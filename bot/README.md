# SoloUno Bot

An scraper bot for PC Components that aims to simplify the SoloTodo API for PC building.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

## Installation

With the installation of the Ubica-tech's Python Project, you are already set to go!

> Just remember to `cd` your way to the bot folder inside the py-ubicatech home folder

## Usage

1. Create a `.env` file with all URLs to be used by the bot, like this:
```sh
cp example.env .env
```
2. Just make sure to select your options and run the `bot` task, for example:
```sh
uv run task bot cpu --socket=lga12
```
The previous command would look for all CPUs with a LGA 1200 socket.

3. (Optional) Run the `help` task to checkout more on the CLI usage.
```sh
uv run task help
```
Which always throws the following output:
```
usage: cli.py [-h] [--socket {lga12,lga17,lga18,am4,am5}] [--ram-type {ddr4,ddr5}] [--case-size {mini-itx,micro-atx,atx,extended-atx}]
              [--ssd-type {sata,nvme}] [--cpu-cooling {liquid,air}] [--fan-size {120,140}] [--psu-cert {bronze,silver,gold,platinum}]
              [--gpu-perf {30,60,90,120}] [--recommended-psu-only] [--min-price MIN_PRICE] [--max-price MAX_PRICE]
              {cpu,mb,ram,hdd,ssd,gpu,pc,cf,box,psu}

Get SoloTodo PC components based on custom constraints and options.

positional arguments:
  {cpu,mb,ram,hdd,ssd,gpu,pc,cf,box,psu}
                        The component type to browse in the SoloTodo API.

options:
  -h, --help            show this help message and exit
  --socket {lga12,lga17,lga18,am4,am5}
                        Socket type of CPU. Available for components: cpu, mb, pc.
  --ram-type {ddr4,ddr5}
                        RAM type. Available for components: ram, mb.
  --case-size {mini-itx,micro-atx,atx,extended-atx}
                        Case size. Available for components: mb, box.
  --ssd-type {sata,nvme}
                        SSD bus type. Available for components: ssd.
  --cpu-cooling {liquid,air}
                        Procesor Cooling type. Available for components: pc.
  --fan-size {120,140}  Case Fan size in mm. Available for components: cf.
  --psu-cert {bronze,silver,gold,platinum}
                        PSU certification. Available for components: psu.
  --gpu-perf {30,60,90,120}
                        GPU performance level on fps high settings. Available for components: gpu.
  --recommended-psu-only
                        Show only recommended brands of PSUs. Available for components: psu.
  --min-price MIN_PRICE
                        Minimum price in USD for the component. Available for all components.
  --max-price MAX_PRICE
                        Maximum price in USD for the component. Available for all components.
```
