<h1>FAQ - High Level</h1>

These are the most frequently asked questions relating to the purpose of Blockly and what it is (and isn't) good for.

(TODO: Add table of contents.)

## How does Blockly relate to Scratch, App Inventor, etc.?

### Similarities

All are [visual programming languages](https://en.wikipedia.org/wiki/Visual_programming_languages).  [Historically](http://web.mit.edu/newsoffice/2010/android-abelson-0819.html), Blockly was influenced by [App Inventor](https://en.wikipedia.org/wiki/App_inventor), and App Inventor was influenced by Scratch, which was influenced by StarLogo and Etoys.

The progenitor of all of these was [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) (not itself a visual programming language), which was co-created by [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert) after working with [Jean Piaget](https://en.wikipedia.org/wiki/Jean_Piaget), one of the proponents of [constructivist learning theory](https://en.wikipedia.org/wiki/Constructivism_(learning_theory)).

### Differences

Rather than being a stand-alone program, Blockly is a code editor that can be embedded into a larger project.  For more information, see the page of [Alternatives](wiki/Alternatives) to Blockly.

## Why are graphics better than text?

Novice programmers are fighting two battles at once: the fight to translate their ideas into logical statements, and the fight to keep the syntax legal.  Blockly makes it completely impossible to make a syntax error.  There are no unbalanced parentheses, no unescaped strings, no missing semicolons.  Blockly allows novice programmers to concentrate on the logic.

Additionally, many non-programmers find a blank screen with a blinking cursor to be daunting.  How does one start?  Blockly allows these users to browse through the menu of blocks and start plugging things together.

Even seasoned programmers can benefit by starting a script with Blockly.  If one is writing a quick script using an unfamiliar API (such as office suite automation) it can take a long time to learn that API.  With Blockly one can plug the blocks together for a first draft, then switch to the generated code to keep going.

## How does Blockly scale to large programs?

It doesn't, at least not yet.  Blockly is currently designed for creating relatively small scripts.  We have ideas for semantic zooming and other techniques that would allow Blockly to scale.  But that is not our current focus.  Please do not attempt to maintain the Linux kernel using Blockly.

## Why not use a data-flow metaphor?

Data-flow is often a simpler way to represent certain common tasks.  However we chose not to use it for two reasons.  The first is that data-flow languages usually fail badly when attempting to solve tasks outside their domain.  The second is that the generated code looks nothing like the visual data-flow representation, which serves as a barrier for the user graduating from the visual programming language to a text-based code editor.  We feel strongly that users should not be locked in.

## Isn't Blockly too low level?

If the user wants to do anything truly original, they must have access to basic math and logic operations.  However, once the basics are taken care of, Blockly offers a rich (and constantly growing) set of higher-level blocks.  Such as computing the standard deviation of a list, using a single block.

Additionally, most of the high-level features would reside in the domain-specific API blocks provided to Blockly by host applications.  For example a game engine using Blockly could have a block that moves a sprite until it hits a wall.

## Can Blockly import from code?

Blockly can export from blocks to JavaScript, Python, and Dart.  However we have no plans to import from one of these languages to Blockly.  The main issue is that modern programming languages are fearsomely complex, with closures, list comprehension, operator overloading, etc.  Importing arbitrary code would have a high development cost compared with a limited real-world utility.

## Can I run Blockly without an Internet connection?

Yes, although you won't be able to save programs for later use.  See [download instructions](http://google.github.io/blockly/hoc.html).

## Why isn't there an installer?

Blockly is a technical preview aimed at application developers.  At this point it is not an end-user application.  Users who are not comfortable with syncing Subversion would most likely be disappointed in the current codebase.  They are encouraged, however, to use our [public server](https://blockly-demo.appspot.com) or to [download a version to run off-line](http://google.github.io/blockly/hoc.html).

## How can I get a young person started with programming?

We recommend trying out the [Hour of Code tutorials](http://code.org/learn).  (The Code.org Angry Birds tutorial uses Blockly.)  If one doesn't appeal to the student, try another.  Many of the tutorial providers have additional material beyond the first hour.

## Why isn't Blockly available in my native language?

Because nobody has [volunteered to translate it yet](wiki/Translation).  Please do so.



---

See also: [Language Design Philosophy](wiki/Language)