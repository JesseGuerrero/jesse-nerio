---
title: "MMORPG Runescape Remake"
excerpt: "A reverse-engineered game based on the original Runescape August 2012 client. Obfuscated Java was manually translated into plain English code and game server was created as a new project.<br/><img src='/images/Runescape.jpg' width='500' height='auto'>"
collection: portfolio
---

## Abstract

Darkan is a comprehensive open-source RuneScape Private Server (RSPS) framework built on the August 2012 client revision 727—the final major pre-Evolution of Combat (EoC) build. Founded in 2013 by Trenton Kress, the project represents one of the most ambitious reverse-engineering efforts in the RSPS community: a developer named Steven spent approximately three years manually translating all ~1,200 obfuscated Java client class files into human-readable, semantically meaningful code. Running on Java 25 LTS, Darkan provides a highly abstracted game development framework that enables developers to create custom RuneScape experiences with minimal code changes. The server architecture supports multi-world lobbies, packet-based networking capable of handling 2,000+ concurrent players per world, and complete content emulation with the notable exception of quests (currently in development). All content is created from scratch, and the framework is designed for eventual full customization.

**Discord**: [https://discord.gg/hxpgC2MGKN](https://discord.gg/hxpgC2MGKN)  
**GitLab**: [https://gitlab.com/darkanrs](https://gitlab.com/darkanrs)  
**Documentation**: [https://darkan.readme.io/docs/getting-started](https://darkan.readme.io/docs/getting-started)  
**Founder**: [Trenton Kress](https://trentonkress.com/)

---

## 1. Introduction

### 1.1 What is an RSPS?

A RuneScape Private Server (RSPS) is a user-created gaming server that emulates the original RuneScape game developed by Jagex. Unlike the official game, an RSPS is operated by independent developers who reverse-engineer the game client and build custom server implementations to handle game logic, networking, and persistence. Key characteristics of RSPS development include:

- **Client Reverse Engineering**: The RuneScape client communicates via proprietary protocols. Developers must analyze obfuscated bytecode to understand packet structures, rendering systems, and game mechanics.
- **Server Emulation**: Since Jagex's server code is never released, RSPS developers write entirely new server implementations in Java (matching the client's language) to handle player connections, game state, and content.
- **Revision System**: Each RuneScape game update produces a new "revision" number. Higher revisions contain more content but are progressively harder to reverse-engineer due to increased obfuscation and complexity.

RSPS projects exist on a spectrum from simple 317-revision servers (circa 2006, well-documented) to complex 700+ revision servers that require extensive reverse-engineering expertise.

### 1.2 The 727 Revision

Revision 727, released in late July/August 2012, represents a particularly significant snapshot of RuneScape's history. This revision captures the game approximately three months before the Evolution of Combat (EoC) update fundamentally changed RuneScape's combat system. Key features present in 727 include:

- Full Dungeoneering skill and Daemonheim content
- God Wars Dungeon with all original bosses
- Nex boss encounter and Ancient Armour (Torva, Pernix, Virtus)
- Queen Black Dragon
- Complete Summoning system
- Player-owned houses (Construction)
- All pre-EoC combat mechanics

The 727 revision is widely considered the most feature-complete "classic" RuneScape experience, making it highly desirable for preservation and emulation efforts.

### 1.3 Project Motivation

Darkan was founded with several core objectives:

1. **Historical Preservation**: Maintain a playable, accurate representation of 2012-era RuneScape
2. **Framework Development**: Create a reusable, well-architected codebase that other developers can extend
3. **Educational Value**: Provide a learning platform for game development, networking, and reverse engineering
4. **Community Building**: Foster collaboration among developers interested in RuneScape emulation

---

## 2. Technical Architecture

### 2.1 System Overview

The Darkan architecture consists of four primary components:

```
┌─────────────────────────────────────────────────────────────────┐
│                        Player Clients                          │
│                   (Deobfuscated 727 Client)                    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Multi-World Lobby                          │
│            (Authentication, World Selection, Social)            │
└─────────────────────────────────────────────────────────────────┘
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
            ┌───────────┐ ┌───────────┐ ┌───────────┐
            │  World 1  │ │  World 2  │ │  World N  │
            │  Server   │ │  Server   │ │  Server   │
            └───────────┘ └───────────┘ └───────────┘
                    │           │           │
                    └───────────┼───────────┘
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        MongoDB Database                         │
│              (Player Data, World State, Persistence)            │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 The Deobfuscation Effort

The foundation of Darkan rests on an extraordinary reverse-engineering achievement. A developer named Steven dedicated approximately three years to manually deobfuscating and translating the entire RuneScape 727 client codebase:

- **~1,200 Java class files** transformed from obfuscated bytecode
- **Variable renaming**: Meaningless identifiers like `a`, `b`, `c` replaced with semantic names (`playerHealth`, `inventorySlots`, `currentAnimation`)
- **Method reconstruction**: Single-letter method names translated to descriptive equivalents
- **Control flow recovery**: Obfuscated jump patterns and dead code removed
- **Documentation**: Key systems annotated with explanations of game mechanics

This deobfuscated client serves as both a reference implementation and the actual game client, enabling developers to understand exactly how the game processes input, renders graphics, and communicates with servers.

### 2.3 Server Architecture

The world server is built on Java 25 LTS, leveraging modern language features while maintaining compatibility with the decade-old client protocol:

**Game Engine Core**:
- Tick-based game loop (600ms cycle matching original RuneScape)
- Entity management system for players, NPCs, and world objects
- Pathfinding algorithms for NPC and player movement
- Combat calculation engine with full pre-EoC mechanics

**Networking Layer**:
- Packet-based TCP/IP communication
- Custom protocol handlers for each of the 200+ packet types
- Connection pooling and session management
- Capacity: 2,000+ concurrent players per world instance

**Content Systems**:
- Skills (all 25 skills fully implemented)
- Combat (Melee, Ranged, Magic with special attacks)
- NPCs (spawning, behavior, drop tables)
- Items (definitions, equipment bonuses, interactions)
- Object interactions (doors, ladders, resource nodes)

### 2.4 Multi-World Lobby System

Darkan implements a multi-world lobby architecture similar to the official game:

```
Player Login Flow:
1. Client connects to Lobby Server
2. Authentication via account credentials
3. World list presented with population counts
4. Player selects world → connection handed off
5. World server receives player session
6. Game state loaded from MongoDB
```

This architecture enables:
- **Horizontal Scaling**: Additional world servers can be deployed independently
- **Social Features**: Friends list and clan systems work across worlds
- **Load Distribution**: Players naturally spread across available worlds

The lobby and social systems remain closed-source to prevent abuse, but public APIs allow developers to spin up their own world servers with minimal configuration.

---

## 3. The Darkan Framework

### 3.1 Abstraction Philosophy

A core design principle of Darkan is high abstraction. The framework is architected so that modifying the RuneScape experience requires minimal code:

**Example: Creating a Custom NPC**
```java
@NPC(id = 1234, name = "Custom Boss")
public class CustomBoss extends CombatNPC {
    
    @Override
    public void onSpawn() {
        setMaxHitpoints(500);
        setCombatLevel(200);
    }
    
    @Override
    public void onDeath(Player killer) {
        killer.sendMessage("You defeated the Custom Boss!");
        dropLoot(killer);
    }
}
```

**Example: Custom Item Effect**
```java
@Item(id = 5678, name = "Magic Amulet")
public class MagicAmulet extends Equipment {
    
    @Override
    public void onEquip(Player player) {
        player.getMagicBonus().addModifier(15);
    }
}
```

The framework handles all underlying complexity—packet encoding, client synchronization, database persistence—allowing developers to focus purely on game content.

### 3.2 Content Completeness

As of the current release, Darkan has achieved remarkable content coverage:

| Category | Status |
|----------|--------|
| Skills (25) | ✓ Complete |
| Combat System | ✓ Complete |
| NPCs & Monsters | ✓ Complete |
| Items & Equipment | ✓ Complete |
| Minigames | ✓ Extensive |
| Quests | ◐ In Development |
| Bosses | ✓ Complete |
| Achievement System | ✓ Complete |

All content has been created from scratch through careful analysis of the original game, Wikipedia research, and community documentation. The quest system represents the final major content category under active development.

### 3.3 Wikipedia Integration

A notable technical feature is the systematic reverse-engineering of RuneScape Wiki data. Game constants, drop tables, NPC statistics, and item properties were extracted and cross-referenced with client data to ensure accuracy. This involved:

- Scraping wiki pages for structured data
- Parsing infobox templates for numerical values
- Validating against observed client behavior
- Integrating into server-side databases

---

## 4. Networking Deep Dive

### 4.1 Packet Protocol

RuneScape communication follows a custom binary protocol over TCP. Each packet consists of:

```
┌────────────┬────────────┬─────────────────────────┐
│  Opcode    │   Size     │        Payload          │
│  (1 byte)  │ (0-2 bytes)│    (variable length)    │
└────────────┴────────────┴─────────────────────────┘
```

**Packet Types**:
- **Fixed**: Predetermined size, no size byte
- **Variable Byte**: 1-byte size field (max 255 bytes)
- **Variable Short**: 2-byte size field (max 65535 bytes)

### 4.2 Key Packet Categories

**Incoming (Client → Server)**:
- Movement packets (walking, running destinations)
- Interface interactions (button clicks, item usage)
- Chat messages and commands
- Combat actions (attack, special attack)

**Outgoing (Server → Client)**:
- Player/NPC updates (position, animation, graphics)
- Interface updates (inventory, skills, chat)
- Region loading (map chunks, objects)
- Audio triggers (sound effects, music)

### 4.3 Player Update Mechanism

The most complex packet type handles player synchronization. Each game tick, the server constructs update packets containing:

1. **Local Player Updates**: Movement, animation, appearance changes for the current player
2. **External Player Updates**: Other visible players' states
3. **Addition/Removal**: Players entering/leaving render distance

This system efficiently compresses data using bit-packing and delta encoding, enabling smooth gameplay even with hundreds of visible players.

### 4.4 Scalability Characteristics

Through careful optimization, each Darkan world server can handle:

- **2,000+ concurrent connections** per instance
- **~16,000 packets/second** throughput
- **600ms tick cycle** maintained under load
- **Sub-50ms packet processing** latency

Horizontal scaling via additional world servers provides effectively unlimited player capacity.

---

## 5. Development Environment

### 5.1 Prerequisites

- Git (version control)
- JDK 25 LTS (or newer)
- MongoDB (player data persistence)
- Gradle (build system)
- IDE (IntelliJ IDEA recommended)

### 5.2 Quick Start

```bash
# Clone repositories
git clone https://gitlab.com/darkanrs/world-server.git
git clone https://gitlab.com/darkanrs/cache.git

# Build and run
cd world-server
gradle run

# Or use the shell script
./run.sh
```

### 5.3 Project Structure

```
darkan/
├── cache/                  # Game asset cache (models, maps, definitions)
├── world-server/           # Main game server
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/darkan/
│   │   │   │   │   ├── engine/       # Core game engine
│   │   │   │   │   ├── network/      # Packet handling
│   │   │   │   │   ├── content/      # Game content
│   │   │   │   │   ├── entity/       # Player/NPC systems
│   │   │   │   │   └── world/        # World management
│   │   │   │   └── ...
│   │   └── resources/
│   └── build.gradle
└── client/                 # Deobfuscated game client
```

---

## 6. Community & Contribution

### 6.1 Open Source Model

Darkan operates under a hybrid open-source model:

**Open Source Components**:
- World server (complete game logic)
- Client source (deobfuscated)
- Cache tools (asset manipulation)
- Documentation

**Closed Source Components**:
- Lobby/Authentication server (security)
- Social services (abuse prevention)

This model encourages contribution while preventing malicious forks that could harm the community.

### 6.2 Contribution Areas

The project welcomes contributions at all skill levels:

- **Beginners**: NPC spawns, drop tables, item definitions, sound effect mapping
- **Intermediate**: Content implementation, bug fixes, documentation
- **Advanced**: Engine improvements, networking optimization, client work

### 6.3 Notable Contributors

- **Trent (Makar)** - Founder, lead developer, hosting/operations
- **Steven** - Three-year client deobfuscation effort
- **Cody (Cody_)** - Client refactoring, cache tools, Fishing Trawler
- **Devin (Durbin)** - Runecrafting systems, Runespan, ZMI altar

### 6.4 Educational Mission

Beyond game development, Darkan serves as an educational platform for:

- Java programming (modern language features)
- Network programming (TCP, binary protocols)
- Game engine design (tick systems, entity management)
- Reverse engineering (bytecode analysis, protocol discovery)
- Database design (MongoDB, data modeling)

---

## 7. Historical Significance

### 7.1 RSPS Landscape Context

Within the RSPS ecosystem, projects are categorized by revision number. Lower revisions (317, 474, 508) have extensive documentation and many public frameworks. Higher revisions present exponentially greater challenges:

| Revision | Era | Documentation | Darkan Position |
|----------|-----|---------------|-----------------|
| 317 | 2006 | Extensive | - |
| 474 | 2007 | Good | - |
| 508 | 2008 | Moderate | - |
| 667 | 2011 | Limited | - |
| **727** | **2012** | **Minimal** | **Most complete framework** |
| 742+ | Post-EoC | Very Limited | - |

Darkan is widely recognized as the most prolific and complete high-revision (above 667) server in existence. No other project has achieved comparable content coverage or code quality at this revision level.

### 7.2 Longevity

Operating continuously since 2013, Darkan represents over a decade of sustained development—a rarity in the RSPS community where projects frequently appear and disappear within months. This longevity demonstrates:

- Sustainable development practices
- Strong community engagement
- Robust technical architecture
- Dedicated maintainership

---

## 8. Future Roadmap

### 8.1 Current Focus

- **Quest System**: The primary content gap, with infrastructure now in place
- **Client Modernization**: Quality-of-life improvements while preserving 727 authenticity
- **Documentation**: Expanding developer guides and API references

### 8.2 Customization Vision

The long-term vision positions Darkan as a fully customizable RuneScape game creation toolkit:

- **Custom Content**: Easy addition of new items, NPCs, areas
- **Rule Modification**: Adjustable XP rates, combat formulas, mechanics
- **Visual Theming**: Client-side asset replacement
- **Plugin System**: Modular content extensions

### 8.3 Community Growth

- Expanded tutorial content for new developers
- Regular development streams/videos
- Formalized contribution guidelines
- Enhanced Discord community structure

---

## 9. Conclusion

Darkan represents a unique intersection of historical preservation, software engineering, and community collaboration. The three-year deobfuscation effort that produced a readable 727 client is itself a remarkable achievement; building a complete, playable game server atop that foundation compounds the accomplishment.

For developers interested in game engine architecture, networking protocols, or reverse engineering, Darkan provides an unparalleled learning opportunity with real, functioning code. For players nostalgic for 2012-era RuneScape, it offers an authentic experience impossible to find elsewhere.

The project's continued evolution toward a fully customizable game creation framework promises to extend its relevance well beyond preservation, enabling entirely new RuneScape-inspired experiences built on battle-tested infrastructure.

### 9.1 Key Achievements

- ✓ Complete ~1,200 file client deobfuscation
- ✓ 10+ years of continuous operation (2013-present)
- ✓ All 25 skills fully implemented
- ✓ 2,000+ player capacity per world
- ✓ Multi-world lobby architecture
- ✓ Open-source world server and client
- ✓ Active development community

### 9.2 Get Involved

Whether you're a seasoned developer or just beginning to learn Java, the Darkan community welcomes participation. Join the Discord to connect with developers, explore the GitLab repositories to examine the code, and consider contributing to this ongoing preservation effort.

---

## Acknowledgments

- **Trenton Kress** - Founder, sustained vision and leadership
- **Steven** - Monumental client deobfuscation work
- **The Darkan Community** - Contributors, testers, and players
- **RuneScape Wiki** - Invaluable reference data
- **Rune-Server Community** - Protocol documentation and research

---

## Technical Stack

- **Language**: Java 25 LTS
- **Database**: MongoDB
- **Build System**: Gradle
- **Version Control**: GitLab
- **Client**: Deobfuscated 727 Java applet
- **Networking**: Custom TCP packet protocol
- **Architecture**: Multi-world lobby with horizontal scaling

---

## Links

- **Discord**: [https://discord.gg/hxpgC2MGKN](https://discord.gg/hxpgC2MGKN)
- **GitLab**: [https://gitlab.com/darkanrs](https://gitlab.com/darkanrs)
- **Documentation**: [https://darkan.readme.io/docs/getting-started](https://darkan.readme.io/docs/getting-started)
- **Founder Website**: [https://trentonkress.com/](https://trentonkress.com/)
