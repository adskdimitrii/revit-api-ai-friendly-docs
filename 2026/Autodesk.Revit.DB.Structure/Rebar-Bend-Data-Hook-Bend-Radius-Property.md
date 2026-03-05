# Rebar Bend Data Hook Bend Radius Property

Source: https://www.revitapidocs.com/2026/2c5d5061-0db2-a2f1-44b5-6bfed651e4f4.htm

---

| Rebar Bend Data Hook Bend Radius Property |
| --- |

The radius of the hook fillets in the Rebar shape.
 The default value is 0\.0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double HookBendRadius { get; set; }
```

```
Public Property HookBendRadius As Double
	Get
	Set
```

```
public:
property double HookBendRadius {
	double get ();
	void set (double value);
}
```

```
member HookBendRadius : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for hookBendRadius is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Inner radius, not centerline ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
