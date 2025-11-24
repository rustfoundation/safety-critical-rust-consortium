# XTask Helper Crate

This crate is used to bundle common checks or helper commands for the repository.

## Check Tooling List

To check that the list of available safety-critical tools still has the correct format, run the following command inside the xtask folder:

```
cargo run -- tool-list verify-format ../subcommittee/tooling/tool-list/available-tools.yaml
```

## Generate Tooling List JSON Schema

To update the JSON schema that describes the format of the tooling list, run the following command inside the xtask folder:

```
cargo run -- tool-list generate-schema ../subcommittee/tooling/tool-list/tool-list-schema.json
```
