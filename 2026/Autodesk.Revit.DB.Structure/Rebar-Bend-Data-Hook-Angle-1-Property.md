# Rebar Bend Data Hook Angle 1 Property

Source: https://www.revitapidocs.com/2026/d9346b7f-10ec-9a28-cdc9-53d9176c9367.htm

---

| Rebar Bend Data Hook Angle 1 Property |
| --- |

The angle (in degrees) of the hook at the end. Must be at least 0 and no more than 180\. If the value is 0 it means that there is no hook.
 The default value is 0\. When setting from 0 to another value all crank lengths for end will be set to 0\.
 When setting this value to 0 HookLength1 will be set to 0\. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int HookAngle1 { get; set; }
```

```
Public Property HookAngle1 As Integer
	Get
	Set
```

```
public:
property int HookAngle1 {
	int get ();
	void set (int value);
}
```

```
member HookAngle1 : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: hookAngle1 must be at least 0 and no more than 180\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
