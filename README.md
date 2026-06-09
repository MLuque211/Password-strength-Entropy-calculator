# Password Strength & Entropy Calculator

This project was developed as the final graduation project for Stanford's **Code in Place 2026**. It is an cybersecurity CLI tool designed to calculate the mathematical entropy of passwords/passphrases and estimate the real world time it would take to crack them using different tiers of computing hardware.

This application provides three core functions:
1. **Password diceware:** Generates secure passphrases using a simulated dice-rolling methodology.
2. **Password analyser:** Tests the user's current password against exhaustive character spaces and strict heuristics.
3. **Password comparison:** Compares a traditional user password directly against a generated diceware passphrase, demonstrating the cognitive and mathematical differences between them.

---
## Features
* **Entropy analysis:** Evaluates exact bits of entropy utilizing Shannon's and (adapted by) Arnold Reinhold entropy formula.
* **Hardware resilience profiling:** Simulates real time brute force and targeted exposure times across three distinct system classes: *Domestic PC*, *Supercomputer*, and an industrial *Hacker farm*.
* **Theoretical vs. real world attack modelling:** Implements adaptive acceleration factors to bridge the gap between ideal mathematical theory and actual modern cracking methodologies.
* **Immersive CLI feedback:** Features custom terminal multicolor visual thermometers and interconnecting physical world security metaphors.
* **Data privacy first:** The program processes inputs strictly within local volatile memory. It does not cache, log, or save any password tested, ensuring absolute user confidentiality. The aim is to understand how they work, not to create them.

---
## Entropy analysis & realism scaling
Mathematically, the tool evaluates standard strings using **Shannon's entropy formula**:
$$E = L \times \log_2(R)$$
Where $L$ is the character string length and $R$ represents the potential character pool size (Lowercase: 26, Uppercase: 26, Numbers: 10, Symbols: 32).

To prevent classic over optimistic time predictions often found in academic examples, this script splits execution analysis into three distinct attack scenarios:
### 1. Theoretical scenario
* **Concept:** Standard mathematical baseline. Assumes an attacker is attempting a blind, sequential, character-by-character brute force attack utilizing single-threaded CPU architectures.
### 2. Real world scenario (hardware acceleration)
* **Factor Applied:** `REAL_ACCELERATION = 1,000`
* **Context:** Real attackers don't leverage general purpose CPUs. They deploy massively parallel Graphic Processing Units (GPUs) or specialized clusters using optimization software like *Hashcat*, *John the Ripper* (with Jumbo patches), *Johnny*,... A mid-to-high tier contemporary GPU tests hashes at rates thousands of times faster than basic CPUs, running these tools tests hashes at rates thousands of times faster than basic CPUs, dropping practical cracking resistance proportionately.
### 3. Predictable pattern scenario (software optimization)
* **Factor Applied:** `PREDICTABLE_REDUCTION = 10,000`
* **Context:** Human password generation is highly non-random. Users inherently lean into predictable heuristics (capitalizing the first character, appending sequence numbers like `123`, or utilizing basic character substitution like *l33tspeak*). Intelligent mask and rule-based dictionary attacks bypass trillions of absurd character combinations, maximizing efficiency over unoptimized brute force.

> [!NOTE]
> Critical Disclaimer on Constraints:
> This tool scales constraints based on character pool distribution. If a 30-character password contains *exclusively* numbers, the raw mathematical space outputs a high "strong" indicator based on character count. However, if a threat actor targets the system specifically utilizing a numeric only library, the actual time to crack would drop immediately to zero. The underlying mathematics inherently differ depending on the explicit generation model used.

>[!CAUTION]
>In short:
>The security of a password never depends solely on its length, but on how unpredictable it is (its entropy) to an attacker. If the attacker discovers the ‘pattern’ (only numbers or sequential patterns or basic dictionary words, for example), the advantage of the length is lost.

---
## The diceware implementation & passphrases
Mathematically, the tool evaluates standard strings using **Arnold Reinhold's entropy formula**. When processing passphrases generated via the *Diceware method*, the mathematical architecture alters completely:
* Search dimensions no longer depend on singular, decoupled characters. Instead, it assumes an atomic pool consisting of the *7,776 distinct words* from the specialized diceware catalog ($6^5$ permutations per five dice rolls).
* The adapted calculation scales as:
$$E = N \times \log_2(7776)$$
Where every randomized word injected introduces exactly **12.92 bits** of pure cryptographic entropy.

A diceware phrase consisting of **5 or more words** establishes severe mathematical resistance even against industrial grade high velocity hacker farms, proving the core cybersecurity paradigm:

>[!NOTE]
>High security, low cognitive load:
>Extremely difficult for an automated machine to brute force, yet incredibly natural for a human mind to retain.

---
## Resources, Attributions & Copyright
The original English wordlist structure and the diceware method provide the foundational framework for this implementation:
* **Author:** Arnold G. Reinhold (Cambridge, Massachusetts, USA).
* **Source:** [The official website diceware][site-url]
* **Official Wordlist Asset:** [Diceware dice indexed word list (PDF)][pdf-url]
* **Copyright:** Copyright © 1995-2026 by Arnold G. Reinhold. All rights reserved.
* **License:** Distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).
* **Warranty disclaimer:** This information is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
* **Contact note:** For inquiries or licensing requests, the author can be reached via electronic mail to: *my initials (three letters) at_sign mac dot com.*

> [!Note]
> The entropy engine, hardware scaling architecture, metric transformation matrices, and user simulation loops are original code authored by me, the developer.

---
## Developer project conclusions (Code in Place - presentation notes)
During development and extensive testing, a few technical challenges and engineering takeaways emerged:
1. **The picosecond paradigm:** Transitioning through vast mathematical scales required tracking performance limits down to picoseconds for weak inputs, all the way up to "Aeons" (billions of years) for strong Diceware phrases.
2. **Big data formatting control:** To keep massive values from truncating or breaking formatting constraints on standard CLI viewports, the Python execution loop implements intelligent notation specifiers (`:.2g` and `:.2e`), dynamically switching presentation types based on numerical extremes.
3. **The balance of security:** Ultimately, a hybrid method provides the best results. While a 121-bit password is mathematically secure, a phrase's safety relies entirely on true structural randomness. If words share logical semantic context, predictability returns. True security requires blending structural length with strict cryptographic chaos.
4. **The realistic speed adaptation:** Moving from pure academic equations to applied security required engineering realistic scaling factors (`REAL_ACCELERATION` and `PREDICTABLE_REDUCTION`). Simulating parallel GPU environments (like _Hashcat_) and predictive human heuristics proved that mathematical theory dramatically overestimates real-world resistance.
5. **The entropy limitation constraint:** A major takeaway was discovering the boundaries of raw mathematical models. A 30-character input composed entirely of numbers outputs a high structural entropy score, yet it offers zero resistance if a threat actor runs a targeted numeric-only library attack. Mathematics must always be evaluated alongside contextual threat vectors.
6. **Confidentiality by design:** To align with professional security standards, the program enforces absolute privacy. Inputs are strictly processed within volatile local memory without generating persistent logs or internal data caching, allowing users to safely test sensitive combinations.
7. **Open source licensing compliance and attribution:** Transitioning to the foundational English Diceware framework highlighted the importance of software legal compliance. Properly attributing the work to its original creator, Arnold G. Reinhold, and documenting the explicit constraints of the *CC BY-NC-ND 4.0* license alongside his original warranty disclaimers ensures a professional deployment standard.
8. **Edge-case structural validation:** Extensive debugging exposed major logical bugs when handling single-word boundaries ($N=1$). This required refactoring the core random injection loops to introduce structural shields, ensuring the program handles extreme data inputs gracefully without dropping runtime errors.
9. **Cross-platform UX/UI terminal compatibility**: Optimizing the visual interface required an architecture that guarantees native portability without external dependencies. By embedding an integrated, lightweight ANSI escape code palette (`CYAN`, `GREEN`, `YELLOW`, `RED`, `MAGENTA`, `WHITE`, `GRAY`) alongside an automated Windows runtime initialization trigger `if os.name == "nt": os.system("")`, the application delivers consistent styling and risk thermometer rendering across UNIX and Windows systems out of the box.
10. **The educational milestone (beginner's perspective)**: Beyond the mathematical modeling and technical adjustments, the entire development lifecycle served as an incredibly rewarding educational milestone. For someone newly entering the software engineering space, building a fully functional, multi-modular cybersecurity calculator from scratch proved to be immensely engaging, challenging, and above all, fun.

---
## Links
[site-url]: https://theworld.com/~reinhold/diceware.html
[pdf-url]: https://theworld.com/%7Ereinhold/dicewarewordlist.pdf

---
*Created as a Final Project for Code in Place 2026.*
