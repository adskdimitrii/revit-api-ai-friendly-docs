# Rebar Bend Data Hook Length 1 Property

Source: https://www.revitapidocs.com/2026/cf4d57e1-01af-f37a-c5c7-af38cb263bd9.htm

---

| Rebar Bend Data Hook Length 1 Property |
| --- |

The extension length of the hook at the end.
 The default value is 0\.0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double HookLength1 { get; set; }
```

```
Public Property HookLength1 As Double
	Get
	Set
```

```
public:
property double HookLength1 {
	double get ();
	void set (double value);
}
```

```
member HookLength1 : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for hookLength1 is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
