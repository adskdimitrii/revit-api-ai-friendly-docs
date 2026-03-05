# Generic Zone Volume Property

Source: https://www.revitapidocs.com/2026/47aa02ad-be47-2443-6307-e57d28a115c7.htm

---

| Generic Zone Volume Property |
| --- |

The volume for the zone, in cubic feet. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double Volume { get; }
```

```
Public ReadOnly Property Volume As Double
	Get
```

```
public:
property double Volume {
	double get ();
}
```

```
member Volume : float with get
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The volume (the gross volume) of a space\-based zone is the sum of the volumes of all spaces in the zone.
 This property will return a value of zero for zones when the volume isn't defined. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
