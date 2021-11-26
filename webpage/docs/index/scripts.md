# Scripts

> Here you should include all of your scripts whether they are text, python notebook or procedural scripts. You should also include link to the link to relevant location in the main pages, description, explanatory materials such as pseudo code or flowcharts, and visualizations if it is applicable. If necessary this page can be broken down to multiple pages. Here is an example of how to include your scripts:

``` python
edges = []
for cell_neigh in cell_neighbors:
    cell = cell_neigh[0]
    for neigh in cell_neigh[1:]:
        if neigh != -1 and neigh > cell:
            edges.append((cell, neigh))
```
