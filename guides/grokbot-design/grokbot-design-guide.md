# Grok Bot for Design

A practical starting point for designing with Grok Bot. Follow eight steps to define a product problem, connect your tools, explore ideas, and prepare a design for implementation.

The guide uses a dashboard feedback card as a running example. Apply the same process to your own screen or component, and replace bracketed prompt details with your project context. Choose your starting point: connect your GitHub repo to work with existing code, or start smaller with screenshots or a product URL. Both paths support design exploration; repository access is needed to change your code or open a pull request.

[Open the interactive guide](https://designproject.io/grokbot-design-guide/)

## 1. Set up your design partner

Install Grok Bot from the official download page and sign in with an eligible paid plan. Check the current account requirements in the official setup instructions before you begin.

Create your first Bot (agent). Give it a name, such as “Design Partner,” and a focused role: helping you explore and improve product designs. Use the prompt below as its role description.

[Official setup instructions](https://docs.x.ai/grok-bot/get-started)

### Try this prompt

```text
Your name is Design Partner. Your role is to help me explore improvements to an existing product, explain design choices in plain language, and show me work I can react to. Start by asking which screen we are improving and what is difficult for its users. We will choose a direction together before implementation.
```

- [ ] My Bot is created and understands its role.

## 2. Connect your GitHub repo, or start with screenshots

Connect your GitHub repository if you want Grok Bot to read the existing code, reuse components, and prepare code changes or pull requests. Paste the repository link into chat and ask it to help you connect. Complete any sign-in and access steps it provides.

No repo access? Start with screenshots or a product URL and a short product brief. You can explore and refine the design, then share an editable design and implementation brief with your team. Changing code or opening a pull request in your repo requires repository access.

### Try this prompt

```text
I’m going to be working in this GitHub repository: [repository URL]. Help me connect it and walk me through any sign-in or access steps. Confirm you can read the project and summarize its structure and existing components before we start designing.
```

- [ ] My repo is connected, or I have chosen to work from screenshots.

## 3. Give it a real product problem

Pick one small part of your product and define what needs to improve. For example, a feedback card might need a clearer status and next action. Tell the Bot who uses the screen, what they need to do, and what already works.

Share your screenshot or product URL, plus your product notes and component library if you have them. Replace the brackets in this prompt.

### Try this prompt

```text
We are improving [screen] in [product]. Our users are [people], and they need to [task]. Today, [specific problem] makes that difficult. A successful change would help them [observable outcome]. Here are the current screen and product notes: [attach files or add links]. Read the available context and summarize the problem before proposing changes. Tell me what information is missing.
```

- [ ] The Bot can explain the user problem accurately.

## 4. Connect the tools for this task

The example workflow uses Mobbin for references, Paper for exploration, and Storybook for existing components. Use the tools that fit your project and connect the ones this task needs. An MCP connection is a way for an AI assistant to work with another tool.

Say which tool you want to use in chat. Grok Bot will guide you through the setup and any sign-in steps. Once connected, ask it to open the file or board you want to work with.

[Official app and connector instructions](https://docs.x.ai/grok-bot/computer-and-apps)

### Try this prompt

```text
I want to use [tool name] for [task]. Help me connect it and walk me through the setup and sign-in steps. Then open [specific file, board, or component] so we can work with it.
```

- [ ] The Bot has opened the exact resources I shared.

## 5. Find references you can actually see

Ask for examples that solve the same interaction problem. Request actual screenshots and source links so you can judge the patterns yourself.

Use Mobbin if you have access, or supply screenshots yourself. Compare how each example communicates status, hierarchy, and the next action.

### Try this prompt

```text
Find three relevant examples of [interaction or UI pattern]. Include the actual screenshots and source links, then explain what each example could help us solve. Put them together in [Paper file or reference board]. Focus on [the information users need to see] and [the action they need to take].
```

- [ ] I can see the references and explain what is useful about them.

## 6. Explore a few directions in Paper

Move from references to alternatives. For a feedback card, you could compare layouts, status pills, and progress indicators. Give the Bot your component library so the exploration stays connected to your product.

Ask for meaningfully different options around one decision. For example: a status pill, a progress indicator, or an action placed directly on the card. Invite the Bot to suggest an alternative based on the product context, rather than only following your first idea.

### Try this prompt

```text
Using our references and existing components, explore three layouts for [screen or component] in [design file]. Prioritize [key information] and make [primary action] easy to find. Vary [the design decision we want to explore] across the options. Show screenshots of the alternatives in chat, link to the editable designs, and explain the tradeoffs. Based on the product context and any connected repository, suggest another direction worth exploring and explain why. Identify any new components we would need.
```

- [ ] I have compared the alternatives and picked a direction.

## 7. Give feedback that changes the design

React to what you can see. Point to the part that is unclear, say why it matters, and describe the behavior you want. Keep the loop small enough to tell whether each change helped.

In this example, the design needs to distinguish feedback that needs review, feedback ready for an agent, and completed work. Compare those states, then place the chosen card in the full dashboard. Check its spacing, hierarchy, and actions alongside the surrounding interface before implementing it.

### Try this prompt

```text
Keep [what works] from option [choice]. Change [specific element] because [user problem]. Make [key information] easier to scan and [next action] easier to find. Show the relevant states together: [list the states for your screen or component]. Place the chosen direction in the full [screen or dashboard], using the surrounding layout and components. Check spacing, hierarchy, and how the actions work in context. Return updated screenshots in chat and the editable link so I can compare them.
```

- [ ] The chosen layout works in the full screen and makes the next action clear.

## 8. Bring the chosen direction into code

Share the exact design you chose and the repository the Bot can work in. Ask it to reuse existing components, tokens, and behaviors. If you do not have repository access yet, finish with the editable design and a short implementation brief for your team.

Review the working result in a browser with your team. Check that the chosen design fits the full screen and that its actions work as expected.

### Try this prompt

```text
Implement the chosen design at [exact design link] in [repository and screen]. First confirm you can access the repository and our Storybook components. Reuse existing tokens and components, and preserve the current actions and data behavior. Work in a separate branch. Show me a working preview, check the relevant states and small-screen layout, run the project checks, and summarize the changed files and anything unresolved. Leave the work ready for team review.
```

- [ ] I have reviewed the working preview or shared an implementation brief.

## No codebase yet?

If you chose the screenshot path in step 2, use this prompt to finish with an editable design and a clear brief for your team.

```text
Prepare an implementation brief for the design we chose. Include the user problem, the design link, the intended behavior for each state, the components to reuse, and the questions our engineering team needs to resolve. Mark assumptions clearly.
```

## Optional: Try a daily planning Bot

The same conversational approach can help with everyday work. Create a separate Bot for calendar planning, connect Google Calendar through the sign-in flow, and ask for a daily agenda with gaps for focused work.

Specify your time zone and review an example before enabling the routine. This is an optional way to explore working across tools from one interface.

```text
Help me connect Google Calendar and walk me through sign-in. Set up a daily briefing for 8 a.m. in [time zone]. List the day’s events and gaps of at least [duration] for focused work. Show me a sample briefing and confirm the schedule before enabling it. Do not create, move, or cancel calendar events.
```

## When you get stuck

### The design looks good but ignores our components.

Give it the exact Storybook or repository location. Ask which existing components it reused and which it created. Revisit the design with that inventory in view.

### The tool connection is unavailable.

Ask the Bot what it can access, then provide screenshots, an export, or an accessible preview. For a sign-in step, follow the app’s authentication flow. Check the official connector instructions below.

## Keep exploring

Keep the prompts, try them on one screen, and see where you need to give the Bot more context or direction.

[Explore TDP workshops](https://tally.so/r/WOPNPP/?utm_source=grokbot_design_guide&utm_medium=resource&utm_campaign=grokbot_design_workshop&utm_content=guide_footer) · [Join the TDP Community](https://designproject.io/community/?utm_source=grokbot_design_guide&utm_medium=resource&utm_campaign=grokbot_design_community&utm_content=guide_footer)

## Official setup resources

Setup checked September 17, 2026. App labels, access, and connector availability can change. The prompts are reusable TDP templates for product design tasks.

- [Grok Bot downloads and access](https://x.ai/bot)
- [Create your first Bot](https://docs.x.ai/grok-bot/get-started)
- [Connect apps and use the Bot’s computer](https://docs.x.ai/grok-bot/computer-and-apps)

Canonical: https://designproject.io/grokbot-design-guide/
