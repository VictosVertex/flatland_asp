# Flatland ASP

Flatland ASP deals with the application of Answer Set Programming techniques to the [Flatland](https://github.com/flatland-association/flatland-rl) environment.

Its first goal is to provide a short introduction to Flatland as well as to Answer Set Programming with the help of documentation and examples.

The second and more exciting goal is to explore various ASP instantiations and encodings of the Flatland environment in order to find solutions to the Problems Flatland tries to help to address.

## Table of Contents

1. [The Vehicle Rescheduling Problem](#1.-the-vehicle-rescheduling-problem)
1. [Flatland](#2-flatland)
   1. [Grid](#21-grid)

## 1. The Vehicle Rescheduling Problem

In a railway system, breakdowns, maintenance issues or other forms of delays may lead to the need for rescheduling vehicles in order to reduce the total delay caused by the disruptive event. The vehicle rescheduling problem (VRSP) is concerned with the optimization of this process, so the minimization of total delay of the network by providing a new optimal plan for all vehicles involved.

Since finding an optimal solution to this problem is NP-Complete but minimal delay is crucial in today's railway networks, other ways of finding sufficiently good solutions have to be explored.

## 2. Flatland

Flatland tries to provide a framework which helps to investigate and test various new approaches to the VRSP. Instead of a complete physics based simulation, Flatland reduces the complexity by simulating agents in a 2D-Grid environment. It provides ways to generate environments, handle agent movements based on action spaces and observations, simulate disruptive events, implement machine learning techniques and more.

### 2.1 Grid

The environment in Flatland is based on a two-dimensional Grid, a matrix of cells
