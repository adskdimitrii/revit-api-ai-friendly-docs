# Bar Terminations Data Termination Rotation Angle At Start Property

Source: https://www.revitapidocs.com/2026/0bcb0dfe-b9c8-d634-ce8d-4053304ef306.htm

---

| Bar Terminations Data Termination Rotation Angle At Start Property |
| --- |

Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the start of bar. 

The default value is 0\. 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double TerminationRotationAngleAtStart { get; set; }
```

```
Public Property TerminationRotationAngleAtStart As Double
	Get
	Set
```

```
public:
property double TerminationRotationAngleAtStart {
	double get ();
	void set (double value);
}
```

```
member TerminationRotationAngleAtStart : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for terminationRotationAngleAtStart is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
