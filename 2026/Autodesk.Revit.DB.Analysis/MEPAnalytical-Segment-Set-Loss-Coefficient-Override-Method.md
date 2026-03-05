# MEPAnalytical Segment Set Loss Coefficient Override Method

Source: https://www.revitapidocs.com/2026/9b1410ea-3287-bed3-3c07-1614b7b92010.htm

---

| MEPAnalytical Segment Set Loss Coefficient Override Method |
| --- |

Sets the overridden value of loss coefficient. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLossCoefficientOverride(
	MEPAnalyticalModelData analyticalModel,
	double lossCoefficient
)
```

```
Public Sub SetLossCoefficientOverride ( 
	analyticalModel As MEPAnalyticalModelData,
	lossCoefficient As Double
)
```

```
public:
void SetLossCoefficientOverride(
	MEPAnalyticalModelData^ analyticalModel, 
	double lossCoefficient
)
```

```
member SetLossCoefficientOverride : 
        analyticalModel : MEPAnalyticalModelData * 
        lossCoefficient : float -> unit 
```

#### Parameters

analyticalModel [MEPAnalyticalModelData](9bb95365-04a3-6c28-5f72-477facd80cbc.htm)
:   The analytical model data that this segment belongs to.

lossCoefficient Double
:   The new loss coefficient value, dimensionless.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
