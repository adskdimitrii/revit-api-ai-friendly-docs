# Rebar Bend Data Hook Length 0 Property

Source: https://www.revitapidocs.com/2026/73f8ee06-a9c1-a869-fcd0-6e1de91eacc9.htm

---

| Rebar Bend Data Hook Length 0 Property |
| --- |

The extension length of the hook at the start.
 The default value is 0\.0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double HookLength0 { get; set; }
```

```
Public Property HookLength0 As Double
	Get
	Set
```

```
public:
property double HookLength0 {
	double get ();
	void set (double value);
}
```

```
member HookLength0 : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for hookLength0 is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
