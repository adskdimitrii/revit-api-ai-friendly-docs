# Bar Terminations Data Termination Rotation Angle At End Property

Source: https://www.revitapidocs.com/2026/aaa56054-7ec8-276b-2cc2-65eac5234239.htm

---

| Bar Terminations Data Termination Rotation Angle At End Property |
| --- |

Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the end of bar. 

The default value is 0\. 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double TerminationRotationAngleAtEnd { get; set; }
```

```
Public Property TerminationRotationAngleAtEnd As Double
	Get
	Set
```

```
public:
property double TerminationRotationAngleAtEnd {
	double get ();
	void set (double value);
}
```

```
member TerminationRotationAngleAtEnd : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for terminationRotationAngleAtEnd is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
