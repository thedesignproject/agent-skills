#!/usr/bin/env node
/**
 * Publish markdown to Ghost CMS
 * Usage: node publish.mjs <markdown-file-path>
 */

import crypto from 'crypto';
import fs from 'fs';
import path from 'path';

// Ghost API credentials from environment variables
const GHOST_URL = process.env.GHOST_URL || "https://ghost.designproject.io";
const ADMIN_API_KEY = process.env.GHOST_ADMIN_API_KEY;

if (!ADMIN_API_KEY) {
  console.error('Error: GHOST_ADMIN_API_KEY environment variable not set');
  console.error('');
  console.error('To fix this:');
  console.error('1. Ask for the Ghost API key in the #general channel on Slack');
  console.error('2. Add it to your ~/.zshrc:');
  console.error('   export GHOST_ADMIN_API_KEY="your-key-here"');
  console.error('3. Run: source ~/.zshrc');
  process.exit(1);
}

// Default author - Dianne Alter
const DEFAULT_AUTHOR_ID = "6430a755ba5a37059cd7760c";

const [id, secret] = ADMIN_API_KEY.split(':');

function createToken() {
  const header = { alg: 'HS256', typ: 'JWT', kid: id };
  const now = Math.floor(Date.now() / 1000);
  const payload = { iat: now, exp: now + 5 * 60, aud: '/admin/' };

  const encodedHeader = Buffer.from(JSON.stringify(header)).toString('base64url');
  const encodedPayload = Buffer.from(JSON.stringify(payload)).toString('base64url');
  const signatureInput = `${encodedHeader}.${encodedPayload}`;
  const signature = crypto
    .createHmac('sha256', Buffer.from(secret, 'hex'))
    .update(signatureInput)
    .digest('base64url');

  return `${signatureInput}.${signature}`;
}

function mdToHtml(md) {
  let html = md;

  // Convert headers with anchors
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+?) \{#\w+\}$/gm, '<h2>$1</h2>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');

  // Convert inline code
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Convert bold and italic
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');

  // Convert links
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  // Process lists line by line
  const lines = html.split('\n');
  let result = [];
  let inUl = false;
  let inOl = false;

  for (const line of lines) {
    const trimmed = line.trim();

    if (trimmed.startsWith('- ')) {
      if (!inUl) {
        if (inOl) { result.push('</ol>'); inOl = false; }
        result.push('<ul>');
        inUl = true;
      }
      result.push(`<li>${trimmed.slice(2)}</li>`);
    }
    else if (/^\d+\. /.test(trimmed)) {
      if (!inOl) {
        if (inUl) { result.push('</ul>'); inUl = false; }
        result.push('<ol>');
        inOl = true;
      }
      result.push(`<li>${trimmed.replace(/^\d+\. /, '')}</li>`);
    }
    else {
      if (inUl) { result.push('</ul>'); inUl = false; }
      if (inOl) { result.push('</ol>'); inOl = false; }
      result.push(line);
    }
  }
  if (inUl) result.push('</ul>');
  if (inOl) result.push('</ol>');

  html = result.join('\n');

  // Convert horizontal rules
  html = html.replace(/^---$/gm, '<hr>');

  // Remove image placeholders
  html = html.replace(/\[IMAGE: [^\]]+\]/g, '');

  // Convert paragraphs
  const paragraphs = html.split(/\n\n+/);
  const processed = paragraphs
    .map(p => p.trim())
    .filter(p => p)
    .map(p => {
      if (p.startsWith('<') || p === '') return p;
      if (/^<(h[1-6]|ul|ol|li|hr|p|div|blockquote)/.test(p)) return p;
      return `<p>${p}</p>`;
    });

  return processed.join('\n\n');
}

async function uploadImage(imagePath) {
  const filename = path.basename(imagePath);
  const fileData = fs.readFileSync(imagePath);

  // Build multipart form data manually (no external deps)
  const boundary = `----FormBoundary${crypto.randomBytes(16).toString('hex')}`;
  const header = Buffer.from(
    `--${boundary}\r\n` +
    `Content-Disposition: form-data; name="file"; filename="${filename}"\r\n` +
    `Content-Type: image/png\r\n\r\n`
  );
  const footer = Buffer.from(`\r\n--${boundary}--\r\n`);
  const body = Buffer.concat([header, fileData, footer]);

  const response = await fetch(`${GHOST_URL}/ghost/api/admin/images/upload/`, {
    method: 'POST',
    headers: {
      'Authorization': `Ghost ${createToken()}`,
      'Content-Type': `multipart/form-data; boundary=${boundary}`,
    },
    body,
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`Image upload failed (${response.status}): ${errText}`);
  }

  const result = await response.json();
  return result.images[0].url;
}

function extractMetadata(content) {
  const metadata = {
    title: '',
    excerpt: '',
    tags: [],
    slug: ''
  };

  // Extract explicit slug from metadata (new SEO field)
  const slugMatch = content.match(/\*\*Slug:\*\*\s*`?([^`\n]+)`?/i);

  // Extract title from first H1
  const titleMatch = content.match(/^# (.+)$/m);
  if (titleMatch) {
    metadata.title = titleMatch[1];
    metadata.slug = slugMatch
      ? slugMatch[1].trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
      : titleMatch[1].toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  // Extract excerpt
  const excerptMatch = content.match(/\*\*Excerpt:\*\*\s*`?([^`\n]+)`?/i);
  if (excerptMatch) {
    metadata.excerpt = excerptMatch[1].trim();
  }

  // Extract tags
  const tagsMatch = content.match(/\*\*Tags:\*\*\s*`?([^`\n]+)`?/i);
  if (tagsMatch) {
    metadata.tags = tagsMatch[1].split(',').map(t => ({ name: t.trim() }));
  }

  return metadata;
}

function extractContent(content) {
  const lines = content.split('\n');
  let contentStart = 0;
  let dashCount = 0;

  // Find content after metadata section (second ---)
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].trim() === '---') {
      dashCount++;
      if (dashCount === 2) {
        contentStart = i + 1;
        break;
      }
    }
  }

  let mainContent = lines.slice(contentStart).join('\n');

  // Remove Content Brief section
  const contentBriefStart = mainContent.indexOf('## Content Brief');
  if (contentBriefStart !== -1) {
    mainContent = mainContent.slice(0, contentBriefStart).trim();
  }

  // Remove Related reading section
  const relatedStart = mainContent.indexOf('## Related reading');
  if (relatedStart !== -1) {
    mainContent = mainContent.slice(0, relatedStart).trim();
  }

  return mainContent;
}

async function publish(filePath) {
  // Resolve file path
  const resolvedPath = path.resolve(filePath);

  if (!fs.existsSync(resolvedPath)) {
    console.error(`Error: File not found: ${resolvedPath}`);
    process.exit(1);
  }

  console.log(`Reading: ${resolvedPath}`);
  const content = fs.readFileSync(resolvedPath, 'utf-8');

  // Extract metadata and content
  const metadata = extractMetadata(content);
  const mainContent = extractContent(content);
  const htmlContent = mdToHtml(mainContent);

  console.log(`Title: ${metadata.title}`);
  console.log(`Slug: ${metadata.slug}`);
  console.log(`Excerpt: ${metadata.excerpt || '(none)'}`);
  console.log(`Tags: ${metadata.tags.map(t => t.name).join(', ') || '(none)'}`);
  console.log(`Content length: ${htmlContent.length} chars`);
  console.log('');

  // Check for a hero image alongside the markdown file
  let featureImageUrl = undefined;
  const mdDir = path.dirname(resolvedPath);
  const mdName = path.basename(resolvedPath, path.extname(resolvedPath));
  const imagePath = path.join(mdDir, `${mdName}.png`);

  if (fs.existsSync(imagePath)) {
    console.log(`Found hero image: ${imagePath}`);
    console.log('Uploading image to Ghost...');
    try {
      featureImageUrl = await uploadImage(imagePath);
      console.log(`Image uploaded: ${featureImageUrl}`);
      console.log('');
    } catch (err) {
      console.error(`Warning: Image upload failed: ${err.message}`);
      console.error('Continuing without feature image...');
      console.log('');
    }
  }

  // Prepare post data
  const postData = {
    posts: [{
      title: metadata.title,
      html: htmlContent,
      status: "draft",
      slug: metadata.slug,
      custom_excerpt: metadata.excerpt || undefined,
      meta_title: metadata.title,
      meta_description: metadata.excerpt || undefined,
      feature_image: featureImageUrl || undefined,
      og_image: featureImageUrl || undefined,
      twitter_image: featureImageUrl || undefined,
      authors: [{ id: DEFAULT_AUTHOR_ID }],
      tags: metadata.tags.length > 0 ? metadata.tags : undefined
    }]
  };

  // Create post with ?source=html parameter
  console.log('Publishing to Ghost...');
  const response = await fetch(`${GHOST_URL}/ghost/api/admin/posts/?source=html`, {
    method: 'POST',
    headers: {
      'Authorization': `Ghost ${createToken()}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(postData)
  });

  if (response.ok) {
    const result = await response.json();
    const post = result.posts[0];
    console.log('');
    console.log('✓ Success! Post created as draft.');
    console.log(`  Title: ${post.title}`);
    console.log(`  Author: Dianne Alter`);
    console.log(`  ID: ${post.id}`);
    console.log('');
    console.log(`Edit in Ghost: ${GHOST_URL}/ghost/#/editor/post/${post.id}`);
  } else {
    console.error(`Error: ${response.status}`);
    console.error(await response.text());
    process.exit(1);
  }
}

// Main
const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: node publish.mjs <markdown-file-path>');
  process.exit(1);
}

publish(filePath);
