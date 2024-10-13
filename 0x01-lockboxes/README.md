# 0x01 Lockboxes

Welcome to the **0x01 Lockboxes** project! This repository contains solutions related to the lockbox problem, a popular coding challenge that involves managing access to locked boxes.

## Project Overview

The lockbox problem involves a series of boxes, each potentially containing keys to other boxes. The objective is to determine if all boxes can be opened given an initial set of keys. This project explores various approaches to solving this problem.

## Problem Statement

You are given `n` boxes, numbered from `0` to `n-1`. Each box may contain keys to other boxes. The task is to determine whether all boxes can be opened starting from box `0`.

## Algorithm

1. **Input Representation**: Each box is represented as a list of keys it contains.
2. **Breadth-First Search (BFS)**: Implement BFS to explore which boxes can be opened with the available keys.
3. **Tracking Opened Boxes**: Maintain a list of opened boxes to ensure each box is processed only once.
