#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author__ = 'Cory Kennedy (cory@darkintel.io)'
#version__ = '2.3'
import fade
import os
import pathlib
import sys

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


class SSC_Banner():

    def ssc_ansi():

        banner_text= """

                ▓▓▓▓▓▓  
             ▓▓▓▓▓▓▓▓▓▓▓▓   
           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
      ▓▓   ▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓ 
   ▓▓▓▓▓   ▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓   ▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓   ▓      ▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓ 
▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▓▓ 
 ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓      
    ▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▒  
▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓ 
▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓      ▒   ▓▓▓▓▓▓▓▓  
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓   ▓▓▓▓▓▓▓▓ 
  ▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓   ▓▓▓▓▓▓  
     ▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓ 
             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                ▓▓▓▓▓▓
                """   
        faded_text = fade.purplepink(banner_text)
        
        def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
            
        # Sort dirs first then by filename
            paths = sorted(
            pathlib.Path(directory).iterdir(),
            key=lambda path: (path.is_file(), path.name.lower()),
        )
            for path in paths:
            # Remove hidden files
                if path.name.startswith("."):
                    continue
                if path.is_dir():
                    style = "dim" if path.name.startswith("__") else ""
                    branch = tree.add(
                        f"[bold magenta]:open_file_folder:[link file://{path}]{escape(path.name)}",
                        style=style,
                        guide_style=style,
                    )
                    walk_directory(path, branch)
                else:
                    text_filename = Text(path.name, "purple")
                    text_filename.highlight_regex(r"\..*$", "bold red")
                    text_filename.stylize(f"link file://{path}")
                    file_size = path.stat().st_size
                    text_filename.append(f" ({decimal(file_size)})", "blue")
                    icon = "🐍 " if path.suffix == ".py" else "📄 "
                    tree.add(Text(icon) + text_filename)
        try:
            directory = os.path.abspath('/Users/coriankennedy/Repositories/ssc-asi-tools')
        except IndexError:
            print("[b]Usage:[/] python tree.py <DIRECTORY>")
        else:
            tree = Tree(
                f":open_file_folder: [link file://{directory}]{directory}",
                guide_style="bold bright_blue",
            )
            walk_directory(pathlib.Path(directory), tree)
            
            panel = Panel(tree,height=24)
            table = Table(title="",box=None, style="cyan")
            table.add_column("", style="cyan")
            table.add_column("", style="magenta",overflow="auto",justify="left")
        
            table.add_row(panel,faded_text)
        
            

        console = Console()
        console.print(table)

                    
   
            
        
banner = SSC_Banner.ssc_ansi
banner()

