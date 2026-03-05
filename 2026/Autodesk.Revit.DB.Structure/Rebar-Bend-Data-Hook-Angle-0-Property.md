# Rebar Bend Data Hook Angle 0 Property

Source: https://www.revitapidocs.com/2026/20652e88-8d2e-b612-8d80-3752ec8f9362.htm

---

| Rebar Bend Data Hook Angle 0 Property |
| --- |

The angle (in degrees) of the hook at the start. Must be at least 0 and no more than 180\. If the value is 0 it means that there is no hook.
 The default value is 0\. When setting from 0 to another value, all crank lengths for start will be set to 0\.
 When setting this value to 0 HookLength0 will be set to 0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int HookAngle0 { get; set; }
```

```
Public Property HookAngle0 As Integer
	Get
	Set
```

```
public:
property int HookAngle0 {
	int get ();
	void set (int value);
}
```

```
member HookAngle0 : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: hookAngle0 must be at least 0 and no more than 180\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
