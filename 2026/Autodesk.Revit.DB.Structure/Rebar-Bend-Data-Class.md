# Rebar Bend Data Class

Source: https://www.revitapidocs.com/2026/027b5619-ad82-74b3-1d78-efe86a1ef96b.htm

---

| Rebar Bend Data Class |
| --- |

The values in this class provide a summary of information taken from the RebarBarType, RebarHookType, and RebarStyle. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarBendData 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarBendData : IDisposable
```

```
Public Class RebarBendData
	Implements IDisposable
```

```
public ref class RebarBendData : IDisposable
```

```
type RebarBendData = 
    class
        interface IDisposable
    end
```
The RebarBendData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RebarBendData](3e725855-09ae-92ef-3d3e-ea26353b1101.htm) | Constructs a new RebarBendData with default settings. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RebarBendData(RebarBarType, RebarStyle, BarTerminationsData)](Rebar-Bend-Data-Rebar-Bar-Type-Rebar-Style-Bar-Terminations-Data-Constructor.md) | Constructs a new RebarBendData using the bar type, style and termination's values. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RebarBendData(RebarBarType, RebarHookType, RebarHookType, RebarStyle, RebarHookOrientation, RebarHookOrientation)](Rebar-Bend-Data-Rebar-Bar-Type-Rebar-Hook-Type-Rebar-Hook-Type-Rebar-Style-Rebar-Hook-Orientation-Rebar-Hook-Orientation-Constructor.md) | **Obsolete.** Constructs a new RebarBendData using the bar type, hook types, style and orientation values. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BarModelDiameter](Rebar-Bend-Data-Bar-Model-Diameter-Property.md) | Defines the model diameter of the bar.  The default value is 0\.0\.  When this is changed, the CrankStraightLength0, CrankStraightLength1, CrankAnledLength0, CrankAnledLength1 will be recomputed. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BarNominalDiameter](Rebar-Bend-Data-Bar-Nominal-Diameter-Property.md) | Defines the nominal diameter of the bar.  The default value is 0\.0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BendRadius](Rebar-Bend-Data-Bend-Radius-Property.md) | The radius of all fillets, except hook fillets, in the Rebar shape.  The default value is 0\.0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankAngledLength0](Rebar-Bend-Data-Crank-Angled-Length-0-Property.md) | Identifies the crank angled length at the start. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankAngledLength1](Rebar-Bend-Data-Crank-Angled-Length-1-Property.md) | Identifies the crank angled length at the end. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankLength0](Rebar-Bend-Data-Crank-Length-0-Property.md) | Identifies the crank length at the start. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankLength1](Rebar-Bend-Data-Crank-Length-1-Property.md) | Identifies the crank length at the end. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankOffsetLength0](Rebar-Bend-Data-Crank-Offset-Length-0-Property.md) | Identifies the crank offset length at the start. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankOffsetLength1](Rebar-Bend-Data-Crank-Offset-Length-1-Property.md) | Identifies the crank offset length at the end. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankRatio0](Rebar-Bend-Data-Crank-Ratio-0-Property.md) | Identifies the crank ratio at the start. The 1:crankRatio that defines the crank slope. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankRatio1](Rebar-Bend-Data-Crank-Ratio-1-Property.md) | Identifies the crank ratio at the end. The 1:crankRatio that defines the crank slope. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankStraightLength0](Rebar-Bend-Data-Crank-Straight-Length-0-Property.md) | Identifies the crank straight length at the start. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CrankStraightLength1](Rebar-Bend-Data-Crank-Straight-Length-1-Property.md) | Identifies the crank straight length at the end. The default value is 0\. A positive value means that there is a valid crank. If the value is 0 it means that there is no crank. If the value is negative it means that there is a crank with incorrect values. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookAngle0](Rebar-Bend-Data-Hook-Angle-0-Property.md) | The angle (in degrees) of the hook at the start. Must be at least 0 and no more than 180\. If the value is 0 it means that there is no hook.  The default value is 0\. When setting from 0 to another value, all crank lengths for start will be set to 0\.  When setting this value to 0 HookLength0 will be set to 0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookAngle1](Rebar-Bend-Data-Hook-Angle-1-Property.md) | The angle (in degrees) of the hook at the end. Must be at least 0 and no more than 180\. If the value is 0 it means that there is no hook.  The default value is 0\. When setting from 0 to another value all crank lengths for end will be set to 0\.  When setting this value to 0 HookLength1 will be set to 0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookBendRadius](Rebar-Bend-Data-Hook-Bend-Radius-Property.md) | The radius of the hook fillets in the Rebar shape.  The default value is 0\.0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookLength0](Rebar-Bend-Data-Hook-Length-0-Property.md) | The extension length of the hook at the start.  The default value is 0\.0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookLength1](Rebar-Bend-Data-Hook-Length-1-Property.md) | The extension length of the hook at the end.  The default value is 0\.0\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookOrient0](Rebar-Bend-Data-Hook-Orient-0-Property.md) | **Obsolete.** Identifies the orientation of the termination (e.g. hook, crank) at the start.  The default value is RebarTerminationOrientation::Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HookOrient1](Rebar-Bend-Data-Hook-Orient-1-Property.md) | **Obsolete.** Identifies the orientation of the termination (e.g. hook, crank) at the end.  The default value is RebarTerminationOrientation::Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](47ad095a-e472-a739-acc9-a99b08b328c6.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientation0](Rebar-Bend-Data-Termination-Orientation-0-Property.md) | Identifies he orientation of the termination (e.g. hook, crank) at the start.  The default value is RebarTerminationOrientation::Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationOrientation1](Rebar-Bend-Data-Termination-Orientation-1-Property.md) | Identifies the orientation of the termination (e.g. hook, crank) at the end.  The default value is RebarTerminationOrientation::Left. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngle0](Rebar-Bend-Data-Termination-Rotation-Angle-0-Property.md) | Identifies the termination's rotation angle (in radians) at the start.  The default value is 0\.0 |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TerminationRotationAngle1](Rebar-Bend-Data-Termination-Rotation-Angle-1-Property.md) | Identifies he termination's rotation angle (in radians) at the end.  The default value is 0\.0 |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](591383a9-1c04-0c9a-07df-78d905caacf3.htm) | Releases all resources used by the RebarBendData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
