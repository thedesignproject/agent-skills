# Grok Bot for Design

A practical starting point for designing with Grok Bot. Follow seven steps to define a product problem, connect your tools, explore ideas, and prepare a design for implementation.

The guide uses a dashboard feedback card as a running example. Apply the same process to your own screen or component, and replace bracketed prompt details with your project context. Start with a screenshot and a clear user need; add your component library and codebase when you are ready.

[Open the interactive guide](https://designproject.io/grokbot-design-guide/)

## 1. Set up your design partner

Install Grok Bot from the official download page and follow its sign-in flow. Create a Bot with one clear job, such as “Design exploration.” Check current account eligibility on the setup page before you begin.

Give it a name and a focused role. You can start with a screenshot of one screen you want to improve.

[Official setup instructions](https://docs.x.ai/grok-bot/get-started)

### Try this prompt

```text
You are my product design partner. Help me explore improvements to an existing product, explain your design choices in plain language, and show me work I can react to. Start by asking which screen we are improving and what is difficult for its users. We will choose a direction together before implementation.
```

- [ ] My Bot is created and understands its role.

## 2. Give it a real product problem

Pick one small part of your product and define what needs to improve. For example, a feedback card might need a clearer status and next action. Tell the Bot who uses the screen, what they need to do, and what already works.

Share your screenshot or product URL, plus your product notes and component library if you have them. Replace the brackets in this prompt.

### Try this prompt

```text
We are improving [screen] in [product]. Our users are [people], and they need to [task]. Today, [specific problem] makes that difficult. A successful change would help them [observable outcome]. Here are the current screen and product notes: [attach files or add links]. Read the available context and summarize the problem before proposing changes. Tell me what information is missing.
```

- [ ] The Bot can explain the user problem accurately.

## 3. Connect the tools for this task

The example workflow uses Mobbin for references, Paper for exploration, and Storybook for existing components. Use the tools that fit your project and connect the ones this task needs. An MCP connection is a way for an AI assistant to work with another tool.

For available connectors, open Settings → Plugins, choose Add, and complete sign-in. Use @ in chat to attach a connector. For a custom MCP connection, ask the Bot to help check the tool’s official setup instructions. Support and access can vary.

[Official app and connector instructions](https://docs.x.ai/grok-bot/computer-and-apps)

### Try this prompt

```text
For this task, I want to use [reference tool], [design tool], and [component library or repository]. Check which connections are available and tell me what I need to do to connect each one. Use the official setup instructions for any MCP. Once connected, confirm you can read [specific file, board, or component]. If you cannot access it, explain what I should provide instead.
```

- [ ] The Bot has opened the exact resources I shared.

## 4. Find references you can actually see

Ask for examples that solve the same interaction problem. Request actual screenshots and source links so you can judge the patterns yourself. If a board only contains descriptions, ask the Bot to add the images before choosing a direction.

Use Mobbin if you have access, or supply screenshots yourself. Compare how each example communicates status, hierarchy, and the next action.

### Try this prompt

```text
Find three relevant examples of [interaction or UI pattern]. Include the actual screenshots and source links, then explain what each example could help us solve. Put them together in [Paper file or reference board]. Focus on [the information users need to see] and [the action they need to take]. If an image is unavailable, say so instead of describing it as if it is on the board.
```

- [ ] I can see the references and explain what is useful about them.

## 5. Explore a few directions in Paper

Move from references to alternatives. For a feedback card, you could compare layouts, status pills, and progress indicators. Give the Bot your component library so the exploration stays connected to your product.

Ask for meaningfully different options around one decision. For example: a status pill, a progress indicator, or an action placed directly on the card.

### Try this prompt

```text
Using our references and existing components, explore three layouts for [screen or component] in [design file]. Prioritize [key information] and make [primary action] easy to find. Vary [the design decision we want to explore] across the options. Show screenshots of the alternatives in chat, link to the editable designs, and explain the tradeoffs. Identify any new components we would need.
```

- [ ] I have compared the alternatives and picked a direction.

## 6. Give feedback that changes the design

React to what you can see. Point to the part that is unclear, say why it matters, and describe the behavior you want. Keep the loop small enough to tell whether each change helped.

In this example, the design needs to distinguish feedback that needs review, feedback ready for an agent, and completed work. Look at all three states together.

### Try this prompt

```text
Keep [what works] from option [choice]. Change [specific element] because [user problem]. Make [key information] easier to scan and [next action] easier to find. Show the relevant states together: [list the states for your screen or component]. Return updated screenshots in chat and the editable link so I can compare them.
```

- [ ] The chosen layout makes the status and next action clear.

## 7. Bring the chosen direction into code

Share the exact design you chose and the repository the Bot can work in. Ask it to reuse existing components, tokens, and behaviors. If you do not have repository access yet, finish with the editable design and a short implementation brief for your team.

The Bot’s cloud computer is separate from your laptop. A local Storybook URL may need a different access route. Ask it to confirm access before it starts, then review the working result in a browser.

[How cloud and local access work](https://docs.x.ai/grok-bot/computer-and-apps)

### Try this prompt

```text
Implement the chosen design at [exact design link] in [repository and screen]. First confirm you can access the repository and our Storybook components. Reuse existing tokens and components, and preserve the current actions and data behavior. Work in a separate branch. Show me a working preview, check the relevant states and small-screen layout, run the project checks, and summarize the changed files and anything unresolved. Leave the work ready for team review.
```

- [ ] I have reviewed the working preview or shared an implementation brief.

## No codebase yet?

Use a screenshot and a short product brief for steps 1–6. Finish with an editable design and hand your team a clear description of what should change.

```text
Prepare an implementation brief for the design we chose. Include the user problem, the design link, the intended behavior for each state, the components to reuse, and the questions our engineering team needs to resolve. Mark assumptions clearly.
```

## When you get stuck

### The reference board only contains descriptions.

Ask for the actual screenshots and source links. If the Bot cannot retrieve them, upload a few examples yourself and ask it to continue from those.

### The design looks good but ignores our components.

Give it the exact Storybook or repository location. Ask which existing components it reused and which it created. Revisit the design with that inventory in view.

### The tool connection is unavailable.

Ask the Bot what it can access, then provide screenshots, an export, or an accessible preview. For a sign-in step, follow the app’s authentication flow. Check the official connector instructions below.

### The preview works, but the real behavior is unclear.

Ask whether the preview uses real data or sample data. Walk through each status and action, and ask the Bot to list any simulated behavior before handing the work to your team.

## Keep exploring

Keep the prompts, try them on one screen, and see where you need to give the Bot more context or direction.

[Explore TDP workshops](https://tally.so/r/WOPNPP/?utm_source=grokbot_design_guide&utm_medium=resource&utm_campaign=grokbot_design_workshop&utm_content=guide_footer) · [Join the TDP Community](https://designproject.io/community/?utm_source=grokbot_design_guide&utm_medium=resource&utm_campaign=grokbot_design_community&utm_content=guide_footer)

## Official setup resources

Setup checked September 15, 2026. App labels, access, and connector availability can change. The prompts are reusable TDP templates for product design tasks.

- [Grok Bot downloads and access](https://x.ai/bot)
- [Create your first Bot](https://docs.x.ai/grok-bot/get-started)
- [Connect apps and use the Bot’s computer](https://docs.x.ai/grok-bot/computer-and-apps)

Canonical: https://designproject.io/grokbot-design-guide/
