# Compound Structure Set Number Of Shell Layers Method

Source: https://www.revitapidocs.com/2026/8b8ea4e3-e697-6176-92c0-dc2687723a71.htm

---

| Compound Structure Set Number Of Shell Layers Method |
| --- |

Sets the number of interior or exterior shell layers. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetNumberOfShellLayers(
	ShellLayerType shellLayerType,
	int numLayers
)
```

```
Public Sub SetNumberOfShellLayers ( 
	shellLayerType As ShellLayerType,
	numLayers As Integer
)
```

```
public:
void SetNumberOfShellLayers(
	ShellLayerType shellLayerType, 
	int numLayers
)
```

```
member SetNumberOfShellLayers : 
        shellLayerType : ShellLayerType * 
        numLayers : int -> unit 
```

#### Parameters

shellLayerType [ShellLayerType](75c640b9-9904-7882-43fc-a4dfc25ff53c.htm)
:   If ShellLayerType.Exterior set the number of exterior shell layers (or top shell layers for a roof, floor, or ceiling type).
 If ShellLayerType.Interior set the number of interior shell layers (or bottom shell layers for a roof, floor, or ceiling type).

numLayers Int32
:   The number of layers to be in the specified shell.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Number of shell layers is negative.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |
| [ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Too many shell layers: Number of shell layers of this type is too large. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Changing this value can result in Core layers becoming Shell layers. This can also result in all Core layers becoming Shell layers and there being an empty core. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
