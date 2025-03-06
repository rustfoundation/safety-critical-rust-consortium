# Safety-Critical Rust Coding Guidelines

_Note_: Early, subject to changes.

## Building the coding guidelines

The Safety-Critical Rust Coding Guidelines use `Sphinx` and `Sphinx-Needs` to build a rendered version of the coding guidelines, and `uv` to install and manage Python dependencies (including Sphinx itself). To simplify building the rendered version, we created a script called `make.py` that takes care of invoking Sphinx with the right flags.

You can build the rendered version by running:

```shell
   ./make.py
```

By default, Sphinx uses incremental rebuilds to generate the content that
changed since the last invocation. If you notice a problem with incremental
rebuilds, you can pass the `-c` flag to clear the existing artifacts before
building:

```shell
   ./make.py -c
```

The rendered version will be available in `build/html/`.

A machine-parseable artifact will be available at `build/html/needs.json`. (ToDo: Pete LeVasseur) The `needs.json` file could use some cleaning up and some description here of the contents.

A record with checksums of the contents is available at `build/html/guidelines-ids.json`. Users of the coding guidelines can reference this file to determine if there have been changes to coding guidelines contents they should be aware of.

## Contributing to the coding guidelines

We have the same chapter layout as the [Ferrocene Language Specification](https://spec.ferrocene.dev/) (FLS). If you would like to contribute you may find a section from the FLS of interest and then write a guideline in the corresponding chapter of these coding guidelines.

### Guideline template

We have a script `./generate-guideline-templates.py` which which assumes you're using `uv` that can be run to generate the template for a guideline with properly randomized IDs.

You can the copy and paste this guideline from the command line into the correct chapter.

### Filling out the guideline

Reference `src/conf.py` to see valid selections for unfilled options in the guideline template.

Note that the `:fls:` option should be filled according to the FLS paragraph ID for which the guideline is covering. One way to go about finding this is to inspect the page using your web browser. You'll be looking for something like:

```html
<p><span class="spec-paragraph-id" id="fls_4rhjpdu4zfqj">4.1:1</span>
```

You would then pull `fls_4rhjpdu4zfqj` to place in the `:fls:` option.

Existing guidelines can also serve as examples on how guidelines are filled.
