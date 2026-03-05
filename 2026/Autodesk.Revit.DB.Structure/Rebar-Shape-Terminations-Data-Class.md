# Rebar Shape Terminations Data Class

Source: https://www.revitapidocs.com/2026/01a81e99-2424-2d06-9d30-dbdb19d05f24.htm

---

| Rebar Shape Terminations Data Class |
| --- |

Class that stores data about rebar shape's terminations (e.g. hooks, cranks, end treatments) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarShapeTerminationsData 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarShapeTerminationsData : IDisposable
```

```
Public Class RebarShapeTerminationsData
	Implements IDisposable
```

```
public ref class RebarShapeTerminationsData : IDisposable
```

```
type RebarShapeTerminationsData = 
    class
        interface IDisposable
    end
```
The RebarShapeTerminationsData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RebarShapeTerminationsData](Rebar-Shape-Terminations-Data-Constructor.md) | Creates a new instance of RebarShapeTerminationData with the default values. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndTreatmentTypeIdAtEnd](Rebar-Shape-Terminations-Data-End-Treatment-Type-Id-At-End-Property.md) | Identifies the end treatement type at the end of the rebar shape.  Setting this property to a valid value, will set the HookAngleAtEnd to 0 and HasCrankAtEnd to false. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndTreatmentTypeIdAtStart](Rebar-Shape-Terminations-Data-End-Treatment-Type-Id-At-Start-Property.md) | Identifies the end treatment type at the start of the rebar shape.  Setting this property to a valid value, will set the HookAngleAtStart to 0 and HasCrankAtStart to false. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HasCrankAtEnd](Rebar-Shape-Terminations-Data-Has-Crank-At-End-Property.md) | Identifies if the rebar shape has crank at end.  Setting this property to true, will set the HookAngleAtEnd to 0 and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HasCrankAtStart](Rebar-Shape-Terminations-Data-Has-Crank-At-Start-Property.md) | Identifies if the rebar shape has crank at start.  Setting this property to true, will set the HookAngleAtStart to 0 and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookAngleAtEnd](Rebar-Shape-Terminations-Data-Hook-Angle-At-End-Property.md) | Identifies the hook angle (in degrees) at the end of the rebar shape.  The angle must be at least 0 and no more than 180\. In case it is 0 it will be considered that the shape doesn't have a hook. Common values are 0, 90, 135, and 180\.  Setting this property to a value strictly greater than 0 and less or almost equal with 180 will set the HasCrankAtEnd to false and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookAngleAtStart](Rebar-Shape-Terminations-Data-Hook-Angle-At-Start-Property.md) | Identifies the hook angle (in degrees) at the start of the rebar shape.  The angle must be at least 0 and no more than 180\. In case it is 0 it will be considered that the shape doesn't have a hook. Common values are 0, 90, 135, and 180\.  Setting this property to a value strictly greater than 0 and less or almost equal with 180 will set the HasCrankAtStart to false and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](Rebar-Shape-Terminations-Data-Is-Valid-Object-Property.md) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientationAtEnd](Rebar-Shape-Terminations-Data-Termination-Orientation-At-End-Property.md) | Identifies the orientation of the termination (e.g. hook, crank) at end. The default value is Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientationAtStart](Rebar-Shape-Terminations-Data-Termination-Orientation-At-Start-Property.md) | Identifies the orientation of the termination (e.g. hook, crank) at start. The default value is Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngleAtEnd](Rebar-Shape-Terminations-Data-Termination-Rotation-Angle-At-End-Property.md) | Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the end of the rebar shape. The default value is 0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngleAtStart](Rebar-Shape-Terminations-Data-Termination-Rotation-Angle-At-Start-Property.md) | Identifies the termination's (e.g. hook, crank) out of plane rotation angle (in radians) at the start of the rebar shape. The default value is 0\. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](Rebar-Shape-Terminations-Data-Dispose-Method.md) | Releases all resources used by the RebarShapeTerminationsData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDocument](Rebar-Shape-Terminations-Data-Get-Document-Method.md) | Gets the document containing the end treatment ids. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
