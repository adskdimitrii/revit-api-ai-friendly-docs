# Bar Terminations Data Properties

Source: https://www.revitapidocs.com/2026/adf59aab-1dfb-2784-f77b-c7b210eb3837.htm

---

| Bar Terminations Data Properties |
| --- |

The [BarTerminationsData](Bar-Terminations-Data-Class.md) type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankTypeIdAtEnd](Bar-Terminations-Data-Crank-Type-Id-At-End-Property.md) | Identifies the crank type at the end of bar.  Setting this property to a valid value, will set the HookTypeIdAtEnd and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankTypeIdAtStart](Bar-Terminations-Data-Crank-Type-Id-At-Start-Property.md) | Identifies the crank type at the start of bar.  Setting this property to a valid value, will set the HookTypeIdAtStart and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndTreatmentTypeIdAtEnd](Bar-Terminations-Data-End-Treatment-Type-Id-At-End-Property.md) | Identifies the end treatment type at the end of bar.  Setting this property to a valid value, will set the CrankTypeIdAtEnd and HookTypeIdAtEnd to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndTreatmentTypeIdAtStart](Bar-Terminations-Data-End-Treatment-Type-Id-At-Start-Property.md) | Identifies the end treatment type at the start of bar.  Setting this property to a valid value, will set the CrankTypeIdAtStart and HookTypeIdAtStart to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookTypeIdAtEnd](Bar-Terminations-Data-Hook-Type-Id-At-End-Property.md) | Identifies the hook type at the end of bar.  Setting this property to a valid value, will set the CrankTypeIdAtEnd and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookTypeIdAtStart](Bar-Terminations-Data-Hook-Type-Id-At-Start-Property.md) | Identifies the hook type at the start of bar.  Setting this property to a valid value, will set the CrankTypeIdAtStart and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](Bar-Terminations-Data-Is-Valid-Object-Property.md) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientationAtEnd](Bar-Terminations-Data-Termination-Orientation-At-End-Property.md) | Identifies the orientation of the termination's (e.g. hook, crank) plane at the end of the bar with respect to the orientation of the last curve and the plane normal. Only two values are permitted: Value \= Right: The termination is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value \= Left: The termination is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." The default value is Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientationAtStart](Bar-Terminations-Data-Termination-Orientation-At-Start-Property.md) | Identifies the orientation of the termination's (e.g. hook, crank) plane at the start of the bar with respect to the orientation of the first curve and the plane normal. Only two values are permitted: Value \= Right: The termination is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value \= Left: The termination is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." The default value is Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngleAtEnd](Bar-Terminations-Data-Termination-Rotation-Angle-At-End-Property.md) | Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the end of bar. The default value is 0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngleAtStart](Bar-Terminations-Data-Termination-Rotation-Angle-At-Start-Property.md) | Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the start of bar. The default value is 0\. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
