# Rebar Hook Type Hook Angle Property

Source: https://www.revitapidocs.com/2026/85af7224-b751-4c40-a5d5-5b4dc757f742.htm

---

| Rebar Hook Type Hook Angle Property |
| --- |

The hook angle, measured in radians. Must be greater than 0\.0174532925 (1 degree) and no more than PI (180 degree). 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double HookAngle { get; set; }
```

```
Public Property HookAngle As Double
	Get
	Set
```

```
public:
property double HookAngle {
	double get ();
	void set (double value);
}
```

```
member HookAngle : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for hookAngle is not a number |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: hookAngle must be greater than 0\.0174532925 (1 degree) and no more than PI (180 degree). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarHookType Class](Rebar-Hook-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
