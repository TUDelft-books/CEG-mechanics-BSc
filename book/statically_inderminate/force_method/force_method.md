```{index} Force method
```

# Apply force method

The force method is treated in in chapter 2.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse (in Dutch) {cite:p}`Hartsuijker2016`.

In the force method, the approach always consists of the followings steps:

1. Determine [the degree of statical determinacy](../determinancy.md).
2. Transform the structure in a statical determinant system by releasing a support, splitting the structure at a two-force member or adding hinges: add unknown statically indeterminate forces and displacement constraints for each of the support you released and hinges you added. Be aware that you don't transform the structure in a (partial) mechanism!

`````{tab-set}
````{tab-item} Releasing a support
```{figure} ./force_method_data/1.svg
:align: center
```
````
````{tab-item} Splitting the structure at a two-force member
```{figure} ./force_method_data/2.svg
:align: center
```
````
````{tab-item} Adding hinges
```{figure} ./force_method_data/3.svg
:align: center
```
````
`````

3. Solve for the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.
4. Use your displacement constraints to solve for the statically indeterminate forces

This chapter includes the following topics:
```{tableofcontents}
```