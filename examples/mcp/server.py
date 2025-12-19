import argparse
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('simple-demo')

@mcp.tool()
def list_files() -> list[str]:
    """Get a list of all the text files on the disk
    
    Returns:
        [str]: An array of all the filenames
    """

    fake_files = ['agents.txt', 'secrets.txt', 'trees.txt']

    return fake_files


@mcp.tool()
def read_data(filename: str) -> str:
    """Read data from a given file

    Args:
        query (str): The filename to get the data from
    
    Returns:
        str: A string containing the file contents
    """

    fake_files = {
        "agents.txt": "Bob\nAlice\nEve",
        "secrets.txt": "five\nsix\nseven\ntwo",
        "trees.txt": "oak\nelm\nbirch"
    }

    return fake_files.get(filename, "File not found")

if __name__ == "__main__":
    print("Starting server")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type", type=str, default="sse", choices=["sse", "stdio"]
    )

    args = parser.parse_args()
    mcp.run(args.server_type)