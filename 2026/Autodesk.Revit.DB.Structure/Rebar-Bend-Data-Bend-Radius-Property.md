# Rebar Bend Data Bend Radius Property

Source: https://www.revitapidocs.com/2026/79f57488-64c6-1630-02a0-b80ceedf510b.htm

---

| Rebar Bend Data Bend Radius Property |
| --- |

The radius of all fillets, except hook fillets, in the Rebar shape.
 The default value is 0\.0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double BendRadius { get; set; }
```

```
Public Property BendRadius As Double
	Get
	Set
```

```
public:
property double BendRadius {
	double get ();
	void set (double value);
}
```

```
member BendRadius : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for bendRadius is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Inner radius, not centerline ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
