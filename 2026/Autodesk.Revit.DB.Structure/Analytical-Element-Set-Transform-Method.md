# Analytical Element Set Transform Method

Source: https://www.revitapidocs.com/2026/a36c9fe3-38ed-65f3-62c6-45c41e086edb.htm

---

| Analytical Element Set Transform Method |
| --- |

Sets the transform of Analytical Element Local Coordinate System. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTransform(
	Transform trf
)
```

```
Public Sub SetTransform ( 
	trf As Transform
)
```

```
public:
void SetTransform(
	Transform^ trf
)
```

```
member SetTransform : 
        trf : Transform -> unit 
```

#### Parameters

trf [Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The provided transformation for Local Coordinate System is not valid. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[AnalyticalElement Class](Analytical-Element-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
