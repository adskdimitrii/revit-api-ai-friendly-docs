# MEPAnalytical Segment Set Override Type Method

Source: https://www.revitapidocs.com/2026/ea12f75f-7bff-500e-7978-d87245303272.htm

---

| MEPAnalytical Segment Set Override Type Method |
| --- |

Sets the override type of pressure loss calculation. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetOverrideType(
	MEPAnalyticalModelData analyticalModel,
	SegmentOverrideType overrideType
)
```

```
Public Sub SetOverrideType ( 
	analyticalModel As MEPAnalyticalModelData,
	overrideType As SegmentOverrideType
)
```

```
public:
void SetOverrideType(
	MEPAnalyticalModelData^ analyticalModel, 
	SegmentOverrideType overrideType
)
```

```
member SetOverrideType : 
        analyticalModel : MEPAnalyticalModelData * 
        overrideType : SegmentOverrideType -> unit 
```

#### Parameters

analyticalModel [MEPAnalyticalModelData](9bb95365-04a3-6c28-5f72-477facd80cbc.htm)
:   The analytical model data that this segment belongs to.

overrideType [SegmentOverrideType](Segment-Override-Type-Enumeration.md)
:   The new override type.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The segment cannot be overridden for the pressure loss calculation. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
