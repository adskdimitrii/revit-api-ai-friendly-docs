# Bar Terminations Data Class

Source: https://www.revitapidocs.com/2026/8a7fb429-e348-5008-b161-d28411cf85d2.htm

---

| Bar Terminations Data Class |
| --- |

Class that stores data about reinforcement's terminations (e.g. hooks, cranks, end treatments) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure BarTerminationsData 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class BarTerminationsData : IDisposable
```

```
Public Class BarTerminationsData
	Implements IDisposable
```

```
public ref class BarTerminationsData : IDisposable
```

```
type BarTerminationsData = 
    class
        interface IDisposable
    end
```
The BarTerminationsData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [BarTerminationsData](Bar-Terminations-Data-Constructor.md) | Creates a new instance of BarTerminationData with the default values. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

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

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsRebarShapeTerminationsData](Bar-Terminations-Data-As-Rebar-Shape-Terminations-Data-Method.md) | Creates a new instance of RebarShapeTerminationsData from this. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](Bar-Terminations-Data-Dispose-Method.md) | Releases all resources used by the BarTerminationsData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDocument](Bar-Terminations-Data-Get-Document-Method.md) | Gets the document containing the hook type ids, end treatment ids and crank type ids. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
