use std::{fs, path::PathBuf};

use clap::Parser;

mod tools_list;

fn main() {
    let cmd = CliCommands::parse();

    match cmd {
        CliCommands::ToolList(tool_cmd) => match tool_cmd {
            ToolListCommands::VerifyFormat(tool_list_verify_format_args) => {
                let file_content =
                    std::fs::read_to_string(tool_list_verify_format_args.tool_list_filepath)
                        .expect("Failed to read tool list file");
                match serde_yaml::from_str::<tools_list::ToolsList>(&file_content) {
                    Ok(tool_list) => {
                        println!(
                            "Verified format for tool list containing '{}' tools.",
                            tool_list.tools.len()
                        );
                    }
                    Err(err) => {
                        eprintln!("Failed to parse tool list file. Cause:\n{err}");
                    }
                }
            }
            ToolListCommands::GenerateSchema(schema_args) => {
                let schema = schemars::schema_for!(tools_list::ToolsList);
                let jsonified = serde_json::to_string_pretty(&schema)
                    .expect("Failed to convert tool list schema to JSON");

                fs::write(schema_args.out_path, jsonified)
                    .expect("Failed to write JSON schema to file");
            }
        },
    }
}

#[derive(Debug, Clone, clap::Parser)]
pub enum CliCommands {
    #[clap(subcommand)]
    ToolList(ToolListCommands),
}

#[derive(Debug, Clone, clap::Subcommand)]
pub enum ToolListCommands {
    VerifyFormat(ToolListVerifyFormatArgs),
    GenerateSchema(ToolListGenSchemaArgs),
}

#[derive(Debug, Clone, clap::Args)]
pub struct ToolListVerifyFormatArgs {
    pub tool_list_filepath: PathBuf,
}

#[derive(Debug, Clone, clap::Args)]
pub struct ToolListGenSchemaArgs {
    pub out_path: PathBuf,
}
