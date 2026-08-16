const lounges = [
  {
    number: 1,
    title: "First Contact",
    tier: "Warm-up",
    description: "Send your first message to an AI model and print what comes back.",
    tags: ["OpenAI API", "Python"],
    icon: "radio",
    accent: "#ffd43b",
    time: "20 min",
    outcome: "A working model conversation",
    path: "../lounge-01-first-contact/README.md",
  },
  {
    number: 2,
    title: "Give It a Personality",
    tier: "Warm-up",
    description: "Shape how your agent speaks, behaves, and responds to people.",
    tags: ["Prompts", "OpenAI API"],
    icon: "message-circle-heart",
    accent: "#ef654f",
    time: "25 min",
    outcome: "An agent with a clear voice",
    path: "../lounge-02-give-it-a-personality/README.md",
  },
  {
    number: 3,
    title: "Write the Rulebook",
    tier: "Core build",
    description: "Create instructions that tell a coding agent what it can and cannot do.",
    tags: ["AGENTS.md", "Rules"],
    icon: "book-open-check",
    accent: "#2ba7b8",
    time: "30 min",
    outcome: "A dependable agent rulebook",
    path: "../lounge-03-write-the-rulebook/README.md",
  },
  {
    number: 4,
    title: "Teach It a Trick",
    tier: "Core build",
    description: "Package a repeatable workflow that your agent can learn and reuse.",
    tags: ["SKILL.md", "Workflows"],
    icon: "wand-sparkles",
    accent: "#6e91d8",
    time: "30 min",
    outcome: "A reusable agent skill",
    path: "../lounge-04-teach-it-a-trick/README.md",
  },
  {
    number: 5,
    title: "Give It Hands",
    tier: "Core build",
    description: "Connect a function so your agent can take action instead of only talking.",
    tags: ["Tools", "Agents"],
    icon: "wrench",
    accent: "#f09a45",
    time: "40 min",
    outcome: "An agent that calls a tool",
    path: "../lounge-05-give-it-hands/README.md",
  },
  {
    number: 6,
    title: "Plug Into MCP",
    tier: "Advanced",
    description: "Let an agent discover, read, and update information through MCP.",
    tags: ["MCP", "Resources"],
    icon: "plug-zap",
    accent: "#52a678",
    time: "45 min",
    outcome: "A connected MCP resource",
    path: "../lounge-06-plug-into-mcp/README.md",
  },
  {
    number: 7,
    title: "Run It With OpenCode",
    tier: "Advanced",
    description: "Give a real coding mission to OpenCode and supervise the whole build.",
    tags: ["OpenCode", "Missions"],
    icon: "terminal-square",
    accent: "#e7c936",
    time: "45 min",
    outcome: "A completed supervised mission",
    path: "../lounge-07-run-it-with-opencode/README.md",
  },
  {
    number: 8,
    title: "Two Robots Talk",
    tier: "Advanced",
    description: "Coordinate two agents and keep their shared conversation in order.",
    tags: ["Multi-agent", "Memory"],
    icon: "messages-square",
    accent: "#c77ab5",
    time: "45 min",
    outcome: "A two-agent conversation",
    path: "../lounge-08-two-robots-talk/README.md",
  },
  {
    number: 9,
    title: "Capstone Showcase",
    tier: "Capstone",
    description: "Combine a personality, a tool, and MCP into one project worth sharing.",
    tags: ["All skills", "Showcase"],
    icon: "presentation",
    accent: "#ef654f",
    time: "60 min",
    outcome: "Your own complete agent",
    path: "../lounge-09-capstone-showcase/README.md",
  },
];

const storageKey = "coding-lounge-progress";
const grid = document.querySelector("#loungeGrid");
const template = document.querySelector("#loungeCardTemplate");
const dialog = document.querySelector("#loungeDialog");
const dialogContent = document.querySelector("#dialogContent");
const continueButton = document.querySelector("#continueButton");

let completed = loadProgress();

function loadProgress() {
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) ?? "[]");
    return new Set(saved.filter((number) => Number.isInteger(number) && number >= 1 && number <= 9));
  } catch {
    return new Set();
  }
}

function saveProgress() {
  localStorage.setItem(storageKey, JSON.stringify([...completed]));
}

function tierKey(tier) {
  return tier.toLowerCase().replaceAll(" ", "-");
}

function renderLounges() {
  grid.replaceChildren();

  lounges.forEach((lounge, index) => {
    const fragment = template.content.cloneNode(true);
    const card = fragment.querySelector(".lounge-card");
    const checkbox = fragment.querySelector("input");
    const icon = fragment.querySelector(".lounge-icon i");

    card.dataset.tier = tierKey(lounge.tier);
    card.dataset.lounge = String(lounge.number);
    card.style.setProperty("--card-accent", lounge.accent);
    card.style.animationDelay = `${index * 45}ms`;
    card.classList.toggle("completed", completed.has(lounge.number));
    fragment.querySelector(".lounge-number").textContent = `LOUNGE ${String(lounge.number).padStart(2, "0")}`;
    fragment.querySelector(".tier-pill").textContent = lounge.tier;
    fragment.querySelector("h3").textContent = lounge.title;
    fragment.querySelector(".lounge-description").textContent = lounge.description;
    icon.dataset.lucide = lounge.icon;

    const tagList = fragment.querySelector(".tag-list");
    lounge.tags.forEach((tag) => {
      const item = document.createElement("span");
      item.className = "tag";
      item.textContent = tag;
      tagList.append(item);
    });

    checkbox.checked = completed.has(lounge.number);
    checkbox.setAttribute("aria-label", `Mark ${lounge.title} complete`);
    checkbox.addEventListener("change", () => toggleComplete(lounge.number, checkbox.checked, card));
    fragment.querySelector(".details-button").addEventListener("click", () => openDetails(lounge));
    grid.append(fragment);
  });

  window.lucide?.createIcons();
  updateProgress();
}

function toggleComplete(number, isComplete, card) {
  if (isComplete) completed.add(number);
  else completed.delete(number);
  card.classList.toggle("completed", isComplete);
  saveProgress();
  updateProgress();
}

function updateProgress() {
  const count = completed.size;
  const percent = Math.round((count / lounges.length) * 100);
  document.querySelector("#progressText").textContent = `${count} of ${lounges.length} complete`;
  document.querySelector("#progressPercent").textContent = `${percent}%`;
  document.querySelector("#progressFill").style.width = `${percent}%`;
  document.querySelector(".progress-track").setAttribute("aria-valuenow", String(count));

  const next = lounges.find((lounge) => !completed.has(lounge.number));
  const label = continueButton.querySelector("span");
  if (next) {
    label.textContent = count ? `Continue lounge ${next.number}` : "Start lounge 1";
    continueButton.onclick = () => {
      requestAnimationFrame(() => document.querySelector(`[data-lounge="${next.number}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" }));
    };
  } else {
    label.textContent = "Journey complete";
    continueButton.onclick = () => openDetails(lounges.at(-1));
  }
}

function openDetails(lounge) {
  dialogContent.innerHTML = `
    <div class="dialog-body">
      <span class="dialog-kicker">Lounge ${String(lounge.number).padStart(2, "0")} · ${lounge.tier}</span>
      <h2 id="dialogTitle">${lounge.title}</h2>
      <p>${lounge.description}</p>
      <div class="dialog-meta">
        <div><span>Build time</span><strong>${lounge.time}</strong></div>
        <div><span>You will make</span><strong>${lounge.outcome}</strong></div>
      </div>
      <a class="dialog-link" href="${lounge.path}">Open the guide <i data-lucide="arrow-right"></i></a>
    </div>`;
  dialog.showModal();
  window.lucide?.createIcons();
}

document.querySelectorAll(".filter").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".filter").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    document.querySelectorAll(".lounge-card").forEach((card) => {
      card.hidden = button.dataset.filter !== "all" && card.dataset.tier !== button.dataset.filter;
    });
  });
});

document.querySelector("#resetButton").addEventListener("click", () => {
  if (!completed.size || !window.confirm("Reset all Coding Lounge progress?")) return;
  completed.clear();
  saveProgress();
  renderLounges();
});

document.querySelector("#dialogClose").addEventListener("click", () => dialog.close());
dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});

renderLounges();