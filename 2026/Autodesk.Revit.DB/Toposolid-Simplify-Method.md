# Toposolid Simplify Method

Source: https://www.revitapidocs.com/2026/dabded04-9e0a-e675-b90e-8b9b0ae7e479.htm

---

| Toposolid Simplify Method |
| --- |

Simplifies the Toposolid by reducing the number of inner vertices to the given percentage. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void Simplify(
	double percentage
)
```

```
Public Sub Simplify ( 
	percentage As Double
)
```

```
public:
void Simplify(
	double percentage
)
```

```
member Simplify : 
        percentage : float -> unit 
```

#### Parameters

percentage Double
:   The ratio of the number of inner vertices after simplify to the original number.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input percentage should be greater than 0 and less than 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | this operation failed. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks At low percentages, the inner vertices may not be reduced to the exact percentage to keep a rough semblance of the original shape.
 Call this method again if you want to keep removing inner vertices. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
