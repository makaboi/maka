const data = {
  origins: ["Castaway", "Lone Warrior", "Vigils", "Etrean", "Deepbound", "Voidwalker", "Tiran", "Khan", "Celtor", "Canor", "Gremor", "Adret", "Vesperian", "Capra", "Felinor"],
  boons: ["Autodidact", "Maverick", "Steadfast", "Survivalist", "Scrapper", "Sly", "Packmule", "Glutton", "Speed Demon", "Cosmetic Expert", "Lootskipper", "Brawler", "Investigator"],
  flaws: ["Vegetarian", "Simple", "Manic", "Squeamish", "Blind", "Obvious", "Hemophilia", "Deficient", "Fugitive", "Claustrophobic", "Moth Eaten", "Glutton", "Frail"],
  attunements: ["Attunementless", "Flamecharm", "Frostdraw", "Galebreathe", "Thundercall", "Shadowcast", "Ironsing", "Bloodrend"],
  weapons: ["Light Weapon", "Medium Weapon", "Heavy Weapon"],
  weaponArchetypes: ["Dagger", "Rapier", "Sword", "Rifle/Spear", "Greataxe", "Greatsword", "Hammer", "Fists"],
  oaths: ["Oathless", "Arcwarder", "Blindseer", "Contractor", "Dawnwalker", "Jetstriker", "Linkstrider", "Silentheart", "Starkindred", "Fadetrimmer", "Bladeharper", "Visionshaper", "Saltchemist", "Chainwarden"],
  stats: ["Strength", "Fortitude", "Agility", "Intelligence", "Willpower", "Charisma", "Weapon", "Attunement"],
  resonances: ["Payback", "Sacred Field", "Run It Back", "Insanity", "Wind-up", "Portals", "Jar of Souls", "Crazy Slots", "Teleportation", "Dimensional Travel", "Gravity Field"],
  murmurs: ["Murmur: Ardour", "Murmur: Rhythm", "Murmur: Tacet", "Murmur: Resolve", "Murmur: Yun'Shul", "Murmur: Courage", "Murmur: Clarity"],
  paths: ["Hero Blade", "Rifle Spear", "Dual Gun", "Frost Tank", "Thunder Speedster", "Flame Crit", "Ironsing Bruiser", "Shadow Mage", "Bleed Duelist"],
  talents: ["Ghost", "Spine Cutter", "Bulldozer", "Kick Off", "Carnivore", "Ether Overdrive", "Perfect Flash", "Nullifying Clarity", "Charged Return", "Brick Wall", "Conditioned Runner", "Observation", "Fishman", "Tough Love", "Last Resort", "Warrior's Respite", "Speed Emission", "Evasive Expert", "Overflowing Dam", "Conquer Your Fears", "Aerial Assault", "Air Counter", "Showstopper", "Unfazed", "Wyvern's Claw", "Swift Rebound", "Million Ton Piercer", "Reaper", "Bloodthirsty", "Needle's Eye", "Tap Dancer", "Thresher Scales", "Lose Your Mind", "Finesse", "All The Dead Gods"],
  legendaryTalents: ["Reinforced Armor", "Exoskeleton", "To The Finish", "Underdog", "Neuroplasticity", "Disbelief", "A World Without Song", "Heretic's Sutra", "Collapsed Lung", "Command: Live", "Brick Wall", "Shared Misery"],
  attunementTalents: {
    Flamecharm: ["Azure Flames", "Flame Wisp", "Emperor Flame", "Lava Serpent", "Burning Servants", "Flame Within"],
    Frostdraw: ["Ice Skate", "Frost Wisp", "Crystal Path", "Frozen Pin", "Chilling Presence", "Thresher Claws"],
    Galebreathe: ["Wind Step", "Aerogliding", "Static Fakeout", "Hurricane Twister Kicks", "Air Force", "Gale Coil"],
    Thundercall: ["Spark Swap", "Lightning Clones", "Static Link", "Jolt Grab", "Thunder Lord", "Supercharge"],
    Shadowcast: ["Dark Rifts", "Black Divers", "Shadow Travel", "Sightless Beam", "Eternal Darkness", "Shade Devour"],
    Ironsing: ["Metal Armament", "Furnace Plate", "Oxidation", "Crystallization", "Reforged", "Alloyblood"],
    Bloodrend: ["Hemoclaw", "Crimson Overflow", "Blood Puppeteer", "Bleed The Vein", "Scarlet Cage", "Sanguine Baptism"],
    Attunementless: ["Strong Left", "Rapid Slashes", "Brace", "Shoulder Bash", "Champions Regalia", "Pressure Blast"]
  },
  mantras: {
    Flamecharm: ["Fire Blade", "Flame Leap", "Ash Slam", "Rising Flame", "Fire Palm", "Flame Repulsion", "Flame Ballista", "Flame Blind", "Burning Servants", "Flame Wisp"],
    Frostdraw: ["Ice Lance", "Warden's Blades", "Frozen Servants", "Ice Fissure", "Glacial Arc", "Ice Cubes", "Ice Smash", "Grand Javelin", "Frost Grab", "Ice Carve"],
    Galebreathe: ["Gale Lunge", "Wind Passage", "Heavenly Wind", "Astral Wind", "Tornado Kick", "Wind Carve", "Air Force", "Pursuit", "Champion's Cyclone", "Gale Trap"],
    Thundercall: ["Jolt Grab", "Lightning Cloak", "Spark Swap", "Thunder Kick", "Lightning Beam", "Grand Support", "Rising Thunder", "Lightning Stream", "Galvanic Arc", "Storm Blades"],
    Shadowcast: ["Shadow Gun", "Rising Shadow", "Shade Bringer", "Eclipse Kick", "Umbral Knight", "Shadow Meteors", "Dark Rift", "Clutching Shadow", "Rising Umbral", "Shadow Eruption"],
    Ironsing: ["Metal Eruption", "Iron Hug", "Forge Warden", "Oxidizing Rush", "Iron Tusk", "Metal Gatling", "Railblade", "Caltrops", "Silver Six", "Reinforced Slam"],
    Bloodrend: ["Blood Scourge", "Sanguine Pull", "Ceaseless Slashes", "Blood Tendrils", "Cruel Cyclone", "Vein Snap", "Hemorrhage", "Crimson Rain", "Blood Volley", "Predatory Slice"],
    Attunementless: ["Shoulder Bash", "Rapid Slashes", "Strong Left", "Champion's Whirlthrow", "Brace", "Revenge", "Adrenaline Surge", "Rapid Punches", "Wayward Gem", "Pressure Drop"]
  }
};

const styleBias = {
  balanced: { boonCount: 2, flawCount: 2, mantraCount: 5, talentCount: 8, attuneTalentCount: 3 },
  pve: { boonCount: 3, flawCount: 2, mantraCount: 5, talentCount: 9, attuneTalentCount: 4 },
  pvp: { boonCount: 2, flawCount: 2, mantraCount: 6, talentCount: 10, attuneTalentCount: 4 },
  caster: { boonCount: 2, flawCount: 1, mantraCount: 8, talentCount: 8, attuneTalentCount: 5 },
  weapon: { boonCount: 2, flawCount: 2, mantraCount: 4, talentCount: 11, attuneTalentCount: 2 },
};

const pickRandom = (arr, n = 1) => [...arr].sort(() => Math.random() - 0.5).slice(0, Math.min(n, arr.length));

function rollStats() {
  const priority = pickRandom(data.stats, 4);
  return priority.map((stat, idx) => `${idx + 1}. ${stat}`);
}

function generateBuild(style) {
  const bias = styleBias[style] || styleBias.balanced;
  const attunement = pickRandom(data.attunements)[0];

  return {
    "Origin & Race Card": pickRandom(data.origins, 2),
    "Boons Card": pickRandom(data.boons, bias.boonCount),
    "Flaws Card": pickRandom(data.flaws, bias.flawCount),
    "Core Path Card": [attunement, pickRandom(data.weapons)[0], pickRandom(data.weaponArchetypes)[0], pickRandom(data.oaths)[0]],
    "Path Fantasy Card": pickRandom(data.paths, 1),
    "Stat Priority Card": rollStats(),
    "Mantras Card": pickRandom(data.mantras[attunement], bias.mantraCount),
    "Attunement Talent Card": pickRandom(data.attunementTalents[attunement], bias.attuneTalentCount),
    "Universal Talent Card": [...pickRandom(data.talents, bias.talentCount - 2), ...pickRandom(data.legendaryTalents, 2)],
    "Resonance Card": pickRandom(data.resonances, 1),
    "Murmur Card": pickRandom(data.murmurs, 1),
  };
}

function renderCards(cards) {
  const output = document.getElementById("buildOutput");
  output.innerHTML = "";
  const tpl = document.getElementById("buildCardTemplate");

  Object.entries(cards).forEach(([title, items]) => {
    const node = tpl.content.cloneNode(true);
    node.querySelector("h2").textContent = title;
    const list = node.querySelector("ul");
    items.forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      list.appendChild(li);
    });
    output.appendChild(node);
  });
}

document.getElementById("generateBtn").addEventListener("click", () => {
  const style = document.getElementById("style").value;
  renderCards(generateBuild(style));
});

renderCards(generateBuild("balanced"));
