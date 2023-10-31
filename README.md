# Flatland ASP

**Flatland ASP** deals with the application of Answer Set Programming techniques to the [Flatland](https://github.com/flatland-association/flatland-rl) environment.

Its first goal is to provide a short introduction to Flatland as well as to Answer Set Programming with the help of documentation and examples.

The second and more exciting goal is to explore various ASP instantiations and encodings of the Flatland environment in order to find solutions to the problems Flatland tries to help to address.

## Table of Contents

1. [The Vehicle Rescheduling Problem](#the-vehicle-rescheduling-problem)
1. [Flatland](#flatland)
   1. [Agents](#agents)
   1. [Grid](#grid)
      1. [Transition Maps](#transition-maps)
      1. [Cell Types](#cell-types)

## The Vehicle Rescheduling Problem

In a railway system, breakdowns, maintenance issues or other forms of delays may lead to the need for rescheduling vehicles in order to reduce the total delay caused by the disruptive event. The vehicle rescheduling problem (**VRSP**) is concerned with the optimization of this process, so the minimization of total delay of the network by providing a new optimal plan for all vehicles involved.

Since finding an **optimal solution** to this problem is **NP-Complete** but minimal delay is crucial in today's railway networks, other ways of finding **sufficiently good solutions** have to be explored.

## Flatland

Flatland tries to provide a **framework** which helps to investigate and test various new approaches to the VRSP. Instead of a complete physics based simulation, Flatland reduces the complexity by simulating agents in a **2D-Grid environment**. It provides ways to **generate environments**, handle **agent movements** based on action spaces and **observations**, simulate **disruptive events**, implement **machine learning** techniques and more.

### Agents

In Flatland **trains** are represented as agents with a specific **position** and **orientation**.
These agents are able to traverse the environment by selecting a single action from their **action space** at each time step. This action space depends on the **transition map** of the cell and the occupation of neighbouring cells by other agents.

Each agent has the goal to travel, optimally with minimal delay, from their starting location to their target location which both are defined by train stations in cities.

### Grid

The grid describes the world in Flatland. It is a matrix of cells of a specific **type** and **orientation** which, using **transition maps**, define if and how an agent can traverse them.

#### Transition Maps

Each **cell's** possible transitions are defined by four 4-bit transition maps. Each map represents an **orientation of an agent** in a specific direction (north, east, south, west) while each bit describes if traversal in one direction is possible or not.

For example the transition maps

`1000 0000 0010 0000`

describe a cell in which a north-oriented agent can go north, a west or east oriented agent can not traverse at all and a south oriented agent can traverse south.

In other words this is a **straight line** going from south to north.

#### Cell types

An **empty cell** is the most basic cell, its transition maps allow no transition and it can't be occupied by an agent at any time. All **other cells represent tracks**, each track cell can be occupied by **at most one agent** at a time.

The different track types are:

- straight lines (south-north)
- simple switches (straight south-north and a south to west turn)
- diamond crossing (two straight lines crossing, **no turns possible**)
- single slip switch (simple switch and diamond crossing)
- double slip switch (diamond crossing, simple switch and a simple switch rotated by 180 degrees)
- symmetrical switch (south-to-west turn, south-to-east turn)
- dead end (**no further traversal** possible, agent **has to turn around**)

These cell types are sufficient to build railway networks of complexity comparable to real-world examples by either using the **base version** as mentioned or use **rotated variants** of these base versions.
