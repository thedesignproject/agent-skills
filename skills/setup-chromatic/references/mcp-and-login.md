# Connect the agent and authenticate

Check current [Chromatic MCP documentation](https://www.chromatic.com/docs/mcp/) and [agent setup](https://www.chromatic.com/docs/agents/) before installing; beta capabilities and supported clients can change. Use installed CLI help to confirm command support. These are connection instructions for the target project, not commands to run while merely authoring this skill.

## Pick one connection path

Prefer Chromatic's official plugin where the user's client supports it. It bundles the account MCP and useful project/build skills. Existing official skills can help connect and inspect projects; do not reimplement them.

Before **any** installation path below, check supported install scope in the client help. Prefer project scope where supported and explain a user/global configuration change before making it. Preserve existing settings and avoid duplicate servers. Their availability does not replace repository setup or CI verification.

**Claude Code**, current documented plugin flow:

```sh
claude plugin marketplace add chromaui/chromatic-plugins
claude plugin install chromatic@chromatic
```

On supported versions, load the installed plugin in the current session with `/reload-plugins`, then open `/mcp`, select Chromatic, and complete browser OAuth. Check the installed client's command support first. These are client UI commands, not shell commands; use a supported host action if available, otherwise ask the user only for those UI steps. Do not require a restart before trying this path. See the current [plugin loading reference](https://code.claude.com/docs/en/plugins/loading). The desktop client may need an initial message before `/mcp` is available.

**Codex**, when installed CLI supports plugins:

```sh
codex plugin marketplace add chromaui/chromatic-plugins
codex plugin add chromatic@chromatic
codex mcp login chromatic
```

Inspect `codex --version` and help first; check the minimum client version in the current Chromatic documentation. Do not upgrade the user's agent automatically just to make this path available.

**Manual MCP alternative**, when plugins are unavailable or unwanted:

```sh
# Claude Code; use the client-supported project scope when appropriate.
claude mcp add --transport http --scope project chromatic https://mcp.chromatic.com/mcp

# Codex; inspect where this client stores configuration before adding.
codex mcp add chromatic --url https://mcp.chromatic.com/mcp
codex mcp login chromatic
```

For Cursor and other clients, use their supported remote MCP settings with Streamable HTTP at **`https://mcp.chromatic.com/mcp`**. Follow the current vendor instructions for plan/admin restrictions. Use an existing authorized installer/settings tool where available. Merge configuration instead of replacing it. Leave OAuth client credentials empty for the account server's supported CIMD flow; do not copy the static client ID intended for a published Storybook MCP.

If the client requires an admin import, lacks remote MCP/CIMD support, or cannot install from this environment, give the smallest specific user action. Do not invent an installer or silently switch clients.

## Login and prove it

- Let the user log in and grant the intended access in their own browser. Do not collect passwords, cookies, or another person's OAuth session.
- Try the installed client's documented reload/reconnect path before a restart. In Claude Code, `/reload-plugins` loads plugin changes; `/mcp` offers Reconnect for an available server. Reconnecting an existing server does not prove a newly added manual configuration has loaded. See [MCP connection management](https://code.claude.com/docs/en/mcp). For Codex and other hosts, discover their supported live refresh; if none exists or tools remain unavailable, explain the specific need for a restart. Do not invent a refresh command or bypass the host through a second agent process.
- After OAuth, rediscover tools and verify authenticated access, then continue the already authorized setup. Before stopping for a restart or login handoff, write and verify the repository-root `CHROMATIC-HANDOFF.md` using [Restart handoff](restart-handoff.md); preserve prior scope, budget, and authorization. On a new-chat request to continue Chromatic, load that file first. Ask only for the actual login/reload/resume interaction required by the client, not a list of future tasks the agent can do itself.
- Discover the actual exposed read-only tools. Use the current documented server-time probe or another exposed read-only call, then verify access to the intended project with a project lookup/listing. A configured URL or successful unauthenticated HTTP request is not proof of login.
- If access is refused for scope, explain the error and use the client's supported reauthentication flow. Do not repeatedly install duplicate servers.

## Provision upload credentials

After login, find/create the project and wire its credentials as part of the authorized setup. Do not make manual secret entry the default handoff.

1. Check approved process environment, secret manager, or ignored local configuration for the correct project's upload token without printing values. Do not scan unrelated credentials or dump env files. A newly created project's one-time token is another valid source; MCP OAuth is not.
2. Detect the CI provider and target repository from the actual remote/workflow. For GitHub, check `gh auth status` and `gh secret list --repo OWNER/REPO` (names/metadata only). Match repository, environment, or organization scope to the workflow. Authentication or a readable repository does not prove secret-write permission; the authorized write's result is decisive.
3. If an appropriate secret already exists, preserve it unless rotation/replacement is authorized. GitHub cannot return its value, so an existing CI secret can support CI verification without enabling a local upload. If publication is authorized, use CI for verification when no local token is available. Otherwise report the local-upload limitation; do not claim it passed.
4. When a token is available and CI-secret setup is authorized, set it yourself with a structured secret-store action, or `gh secret set CHROMATIC_PROJECT_TOKEN --repo OWNER/REPO` reading the value from stdin. Use the actual workflow's secret name; keep separate names for both lanes. Feed stdin from the approved secret source through a secure process API/pipe; never use `--body`, literal shell interpolation, debug tracing, or a command containing the token. Do not pipe an entire env file or use bulk import that changes unrelated secrets. If the host cannot transfer a token securely, use its secret-entry UI instead.
5. Verify the write succeeded and the expected secret name/scope exists without displaying its value. Check a real upload/CI result to prove the token works. For local CLI runs, pass the approved token through the subprocess environment without logging it; GitHub's stored secrets cannot be downloaded for this purpose.
6. On missing `gh`, authentication, token, permission, or secure input support, explain exactly which is missing. Use available authorized alternatives, then ask only for the remaining user action, such as browser authentication or secure token entry. Do not request passwords or tokens in chat, recreate projects to obtain tokens, or broaden account permissions automatically.

Secret writes are external changes. Respect local-only restrictions and the user's chosen scope; an end-to-end setup that explicitly includes CI-secret provisioning does not need a fresh permission question after OAuth or restart. Account/host consent prompts remain user actions. See [GitHub's secret-set documentation](https://cli.github.com/manual/gh_secret_set) for stdin and scope options.

## Tool boundaries

The MCP can inspect account/project/build data and has mutations such as project creation and test decisions. It cannot itself run a build, change project feature settings, retrieve an existing project's upload token, or post/resolve reviewer replies. Use CLI/CI for builds and the supported web settings when necessary. Project creation can return its token once in the tool result. Store that sensitive value through an authorized secret field or stdin; never echo it, interpolate it into a shell command, or put it in a resume note. The upload CLI needs a separate project token; MCP OAuth login does not supply that credential to the CLI.

Keep visual acceptance manual unless the user explicitly delegates it. Never quarantine tests or dismiss differences to get a green setup.

The separate Storybook MCP at a published Storybook's `/mcp` route is a component documentation service. Do not substitute it for the account MCP or enable it merely because the user chose component visual tests.
