# Compound Structure Get Number Of Shell Layers Method

Source: https://www.revitapidocs.com/2026/68e04211-03ea-f0c6-50d5-b38fee4e7536.htm

---

| Compound Structure Get Number Of Shell Layers Method |
| --- |

Retrieves the number of interior or exterior shell layers. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int GetNumberOfShellLayers(
	ShellLayerType shellLayerType
)
```

```
Public Function GetNumberOfShellLayers ( 
	shellLayerType As ShellLayerType
) As Integer
```

```
public:
int GetNumberOfShellLayers(
	ShellLayerType shellLayerType
)
```

```
member GetNumberOfShellLayers : 
        shellLayerType : ShellLayerType -> int 
```

#### Parameters

shellLayerType [ShellLayerType](75c640b9-9904-7882-43fc-a4dfc25ff53c.htm)
:   If ShellLayerType.Exterior return the number of exterior shell layers (or top shell layers for a roof, floor, or ceiling type).
 If ShellLayerType.Interior return the number of interior shell layers (or bottom shell layers for a roof, floor, or ceiling type).

#### Return Value

Int32 
The number of shell layers in the interior or exterior shell, as specified by shellLayerType. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks There could be no core layers. You can change the shell/core layer boundary using [SetNumberOfShellLayers(ShellLayerType, Int32\)](Compound-Structure-Set-Number-Of-Shell-Layers-Method.md) . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
