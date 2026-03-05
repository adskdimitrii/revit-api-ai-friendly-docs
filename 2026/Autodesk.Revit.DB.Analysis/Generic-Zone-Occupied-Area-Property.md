# Generic Zone Occupied Area Property

Source: https://www.revitapidocs.com/2026/2417b6c9-da20-253f-e105-ff45cc216853.htm

---

| Generic Zone Occupied Area Property |
| --- |

The occupied area for the zone, in square feet. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double OccupiedArea { get; }
```

```
Public ReadOnly Property OccupiedArea As Double
	Get
```

```
public:
property double OccupiedArea {
	double get ();
}
```

```
member OccupiedArea : float with get
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The occupied area of a space\-based zone is the sum of the areas of the spaces marked Occupiable in the zone.
 This property will return a value of zero for zones where this type of area isn't applicable. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
