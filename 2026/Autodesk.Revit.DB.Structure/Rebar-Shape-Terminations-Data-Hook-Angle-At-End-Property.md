# Rebar Shape Terminations Data Hook Angle At End Property

Source: https://www.revitapidocs.com/2026/cb747aed-3f84-6452-1332-41d25cf00f15.htm

---

| Rebar Shape Terminations Data Hook Angle At End Property |
| --- |

Identifies the hook angle (in degrees) at the end of the rebar shape.
 The angle must be at least 0 and no more than 180\. In case it is 0 it will be considered that the shape doesn't have a hook. Common values are 0, 90, 135, and 180\.
 Setting this property to a value strictly greater than 0 and less or almost equal with 180 will set the HasCrankAtEnd to false and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int HookAngleAtEnd { get; set; }
```

```
Public Property HookAngleAtEnd As Integer
	Get
	Set
```

```
public:
property int HookAngleAtEnd {
	int get ();
	void set (int value);
}
```

```
member HookAngleAtEnd : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: hookAngleAtEnd must be at least 0 and no more than 180\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeTerminationsData Class](Rebar-Shape-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
