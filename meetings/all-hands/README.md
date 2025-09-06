## Safety Critical All-Hands Meetings

### Purpose

The Safety-Critical Rust Consortium's monthly All-Hands meetings are an opportunity for Rust or general safety-critical developers to stay up-to-date with the latest news from safety-critical Rust, new tools or projects, and the activities of the consortium itself. They will also provide an opportunity for the consortium to solicit volunteers or call attention to open-source or commercial opportunities.

All-Hands occur monthly but rotate through three global time slots, to offer convenient times for all time zones. Due to this, each meeting will have some content overlap with the prior two given the expectation that most consortium members will attend only quarterly.

### Agenda

The agenda for each meeting is loosely grouped into:

1. **Quarterly Summary**  
  A brief synopsis of topics covered in prior meetings.
2. **General Rust Safety Critical News**  
  News from the world of safety critical Rust such as companies adopting the language, new tools or open-source projects, or breakthroughs in implementation (new certifications, etc).
3. **Subcommittee Reports**  
  Brief updates from each of the subcommittees regarding what they've been working on or their challenges/needs from the community.
4. **Calls to Action**  
  A request for volunteers to aid in consortium activities, highlights of gaps in safety-critical tooling that are market opportunities, or requests for open-source contributors or maintainers.

### Process

The agenda for each All-Hands will be developed in Pull Requests here in the Safety Critical Consortium repo. A branch will be opened for each meeting along with a draft PR against `main`. The agenda and slides can be developed with PRs against the all-hands branch, in comments on the draft PR, or in issues for anything more general.

Contributors are welcome to build slides directly or suggest topics (such as a news story or tool release) that can then be integrated into the slides. Once the meeting is complete the slides will be exported to a static format and the PR will be merged into main as an archive.

### Slides

We're using [presenterm](https://github.com/mfontanini/presenterm) for the slides. This is a program (written in Rust!) that translates a markdown formatted document into a slideshow. It can either present directly within a terminal or export to files. This keeps the content directly within the repo, not as unversioned data stored in Google Slides. It allows us to develop the slide content in public and through the PR mechanism, and keeps them archived alongside the rest of the consortium content.

> [!NOTE]
> While basic text rendering is available in all terminals, for images to be rendered inline a GPU based terminal emulator is required. Some options include [Ghostty](https://ghostty.org/) or [kitty](https://sw.kovidgoyal.net/kitty/).

The [presenterm docs](https://mfontanini.github.io/presenterm/) contain all the necessary information to install the tool, edit the slides, and run a presentation. But in brief:

1. Install from source using `cargo install --locked presenterm` or install [a built package using your OS' distro manager](https://mfontanini.github.io/presenterm/install.html).  
2. Edit the presentation with all markdown syntax and some additional command tags:
  - `<!-- end_slide -->` marks the boundary between two slides
  - `<!-- pause -->` sets a pause between displaying content on a single slide
  - `<!-- jump_to_middle -->` centers content within the middle of the slide vertically, useful for titles or subtitles
3. Navigate to a directory with a markdown presentation and start the slideshow with `presenterm -p [filename.md]`.
4. Alternatively the presentation can be exported to a PDF with `presenterm -e [filename.md]`. Or to an HTML document with `presenterm -E [filename.md]`.