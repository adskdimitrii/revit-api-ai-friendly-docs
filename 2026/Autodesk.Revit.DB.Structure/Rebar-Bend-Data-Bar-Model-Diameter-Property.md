# Rebar Bend Data Bar Model Diameter Property

Source: https://www.revitapidocs.com/2026/ab0a3aff-ec87-f6e4-1151-ada0b735b3d9.htm

---

| Rebar Bend Data Bar Model Diameter Property |
| --- |

Defines the model diameter of the bar.
 The default value is 0\.0\.
 When this is changed, the CrankStraightLength0, CrankStraightLength1, CrankAnledLength0, CrankAnledLength1 will be recomputed. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double BarModelDiameter { get; set; }
```

```
Public Property BarModelDiameter As Double
	Get
	Set
```

```
public:
property double BarModelDiameter {
	double get ();
	void set (double value);
}
```

```
member BarModelDiameter : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for barModelDiameter is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
