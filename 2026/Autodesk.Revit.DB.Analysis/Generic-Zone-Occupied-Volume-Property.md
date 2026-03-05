# Generic Zone Occupied Volume Property

Source: https://www.revitapidocs.com/2026/001024e5-1818-7f2d-d7a2-1e17a80ee62e.htm

---

| Generic Zone Occupied Volume Property |
| --- |

The occupied volume for the zone, in cubic feet. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double OccupiedVolume { get; }
```

```
Public ReadOnly Property OccupiedVolume As Double
	Get
```

```
public:
property double OccupiedVolume {
	double get ();
}
```

```
member OccupiedVolume : float with get
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The occupied volume of a space\-based zone is the sum of the volumes of the spaces marked Occupiable in the zone.
 This property will return a value of zero for zones where this type of volume isn't applicable. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
