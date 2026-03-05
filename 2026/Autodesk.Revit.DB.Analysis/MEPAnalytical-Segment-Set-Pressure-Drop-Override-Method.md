# MEPAnalytical Segment Set Pressure Drop Override Method

Source: https://www.revitapidocs.com/2026/c3223ca1-82b5-85e5-93c3-628b158ae5a3.htm

---

| MEPAnalytical Segment Set Pressure Drop Override Method |
| --- |

Sets the overridden value of pressure drop. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetPressureDropOverride(
	MEPAnalyticalModelData analyticalModel,
	double pressureDrop
)
```

```
Public Sub SetPressureDropOverride ( 
	analyticalModel As MEPAnalyticalModelData,
	pressureDrop As Double
)
```

```
public:
void SetPressureDropOverride(
	MEPAnalyticalModelData^ analyticalModel, 
	double pressureDrop
)
```

```
member SetPressureDropOverride : 
        analyticalModel : MEPAnalyticalModelData * 
        pressureDrop : float -> unit 
```

#### Parameters

analyticalModel [MEPAnalyticalModelData](9bb95365-04a3-6c28-5f72-477facd80cbc.htm)
:   The analytical model data that this segment belongs to.

pressureDrop Double
:   The new pressure drop value, in kg/(ft\*s^2\). Note that the negative value indicates the pressure gain at the flow direction.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
