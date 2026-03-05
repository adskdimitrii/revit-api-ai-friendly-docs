# Rebar Bend Data Bar Nominal Diameter Property

Source: https://www.revitapidocs.com/2026/4af85f50-5725-36fb-dedc-972639ed4c5c.htm

---

| Rebar Bend Data Bar Nominal Diameter Property |
| --- |

Defines the nominal diameter of the bar.
 The default value is 0\.0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double BarNominalDiameter { get; set; }
```

```
Public Property BarNominalDiameter As Double
	Get
	Set
```

```
public:
property double BarNominalDiameter {
	double get ();
	void set (double value);
}
```

```
member BarNominalDiameter : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for barNominalDiameter is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
