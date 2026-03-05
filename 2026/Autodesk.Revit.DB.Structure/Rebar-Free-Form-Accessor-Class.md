# Rebar Free Form Accessor Class

Source: https://www.revitapidocs.com/2026/bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm

---

| Rebar Free Form Accessor Class |
| --- |

A class that is used to access the properties and capabilities of free\-form Rebar. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarFreeFormAccessor 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarFreeFormAccessor : IDisposable
```

```
Public Class RebarFreeFormAccessor
	Implements IDisposable
```

```
public ref class RebarFreeFormAccessor : IDisposable
```

```
type RebarFreeFormAccessor = 
    class
        interface IDisposable
    end
```
The RebarFreeFormAccessor type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AlignedFreeFormSetOrientationOptions](052bb659-79b5-60ca-c683-c2e45c3882cd.htm) | Orientation options for an Aligned Free Form Rebar set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CycleCounter](dc7ccd08-60d5-3cc8-e99a-66e87cbdbc13.htm) | Identifies the cycle counter. It can be zero or a pozitive number. Its value is changed when the free form Rebar element is selected and the user press Space key  \-or\- through the setter of this property  \-or\- by the server if it considers that the counter reaches the maximum value and reset it (set it to 0\).  This property can be accessed just for Rebars that are controlled by a server. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](491dc896-0fac-c1b2-af22-3aeee04fac1a.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RebarStyle](d44af128-695b-272f-d396-24618c0bb2dc.htm) | Identifies the RebarStyle of the current Rebar element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [StirrupTieAttachmentType](bc9bdd47-9bc4-6d13-7a03-94b568fdad24.htm) | Identifies the StirrupTieAttachmentType of the current Rebar element.  The RebarStyle of the Rebar element must be StirrupTie. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [WorkshopInstructions](767b1bab-6fc4-92b1-3caa-0090c83faccb.htm) | Identifies the workshop instructions of the current Rebar element. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddUpdatingSharedParameter](6401f06c-476d-bacd-6173-9c7948d286ce.htm) | Add existing shared parameter as a dependency for the calculation of the rebar curves. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeHookNormal](Rebar-Free-Form-Accessor-Can-Be-Hook-Normal-Method.md) | **Obsolete.** A vector can be termination's (e.g. hook, crank) normal if for a bar specified by index, the bar direction is not parallel with the vector. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeTerminationPlaneNormal](Rebar-Free-Form-Accessor-Can-Be-Termination-Plane-Normal-Method.md) | A vector can be termination (e.g. hook, crank) plane normal if for a bar specified by index, the bar direction is not parallel with the vector. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DisconnectFromServer](0eab1821-30f3-19c9-05b0-fa7c08b6e038.htm) | Sets the GUID of the API server to invalid value and removes all the server related data from the Rebar (ex. the current constraints and the handle tags are removed).  Calling this method will result in a Rebar that will not react to host changes anymore, however it will still have all the properties that it used to have. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](1fba9ff6-d5b4-937b-10fb-9d50b71c9e9a.htm) | Releases all resources used by the RebarFreeFormAccessor |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCouplerIdAtIndex](aeed9fe2-0225-4940-0914-a47a9e6c61d5.htm) | Gets the id of the Rebar Coupler that is applied to the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCrankTypeIdAtIndex](Rebar-Free-Form-Accessor-Get-Crank-Type-Id-At-Index-Method.md) | Gets the id of the Rebar Crank Type that is applied to this Rebar at the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCustomDistributionPath](122a818c-2a81-ff20-2435-67b19e20e5af.htm) | Gets the custom distribution path for free form rebar set. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEndTreatmentTypeIdAtIndex](12bf4634-9e2c-08c3-5aa2-54f796651c70.htm) | Gets the id of the EndTreatmentType that is applied to the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookOrientationAngle](Rebar-Free-Form-Accessor-Get-Hook-Orientation-Angle-Method.md) | **Obsolete.** Get the termination's rotation angle at end.  The angle is used for both hook and crank. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookOrientationAngleAtIndex](Rebar-Free-Form-Accessor-Get-Hook-Orientation-Angle-At-Index-Method.md) | **Obsolete.** Gets the termnination's rotation angle that is applied to this Rebar at the bar with index barPositionIndex at the specified end.  The rotation angle it's the same for both hook and crank. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookOrientationAtIndex](Rebar-Free-Form-Accessor-Get-Hook-Orientation-At-Index-Method.md) | **Obsolete.** Gets the termination's orientation that is applied to this Rebar at the bar with index barPositionIndex at the specified end.  The orientation it's the same for both hook and crank. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookPlaneNormalForBarIdx](Rebar-Free-Form-Accessor-Get-Hook-Plane-Normal-For-Bar-Idx-Method.md) | **Obsolete.** Returns the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay.  The plane's normal is used for both hook and crank. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookTypeIdAtIndex](27a70740-3367-6509-aeae-e58fb578e763.htm) | Gets the id of the RebarHookType that is applied to this Rebar at the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetServerGUID](10a19cd7-d552-6382-262b-4bf268957821.htm) | Returns the GUID of the API server. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetShapeIdAtIndex](79172a28-c9c1-3659-681f-f365ba834f03.htm) | Gets the Rebar Shape id for the bar with index barPositionIndex. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTerminationOrientationAtIndex](Rebar-Free-Form-Accessor-Get-Termination-Orientation-At-Index-Method.md) | Gets the termination's (e.g. hook, crank ) orientation that is applied to this Rebar at the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTerminationPlaneNormalForBarIndex](Rebar-Free-Form-Accessor-Get-Termination-Plane-Normal-For-Bar-Index-Method.md) | Gets the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTerminationRotationAngleAtIndex](Rebar-Free-Form-Accessor-Get-Termination-Rotation-Angle-At-Index-Method.md) | Gets the termination (e.g hook,crank) rotation angle that is applied to this Rebar at the bar with index barPositionIndex at the specified end. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetUpdatingSharedParameters](7a5ecdb0-a5cd-e64b-1640-c4c03cd16a25.htm) | Get the shared parameters listed as dependencies in the calculation of the rebar curves |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasValidAlignedServer](7ada7359-1303-4a2e-d276-c93567f2bdce.htm) | Returns true if the current rebar is created with the Aligned Free Form rebar server, false otherwise. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasValidServer](be45e502-8cce-5dec-709d-38cfcc9e91d2.htm) | Returns true if the current rebar contains a valid server GUID, false otherwise. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsBarMatchedWithShapeInReverseOrder](4e8d66b4-8a27-200a-e7d5-8cd8bec7c34b.htm) | Checks if the bar at index barPositionIndex it's matched in reversed order with its shape. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsUnconstrained](4999e26b-8de2-5db8-ddbf-12e98184773e.htm) | Returns true if the current rebar doesn't contains a valid server GUID, or contains a valid server GUID and no valid constraints. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveUpdatingSharedParameter](17cac627-4846-e71d-b181-6ea6ef7d5257.htm) | Remove existing shared parameter as a dependency for the calculation of the rebar curves. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetCurves(IList CurveLoop )](8ca32c92-c297-84db-ffdc-8ab2017d6b98.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetCurves(IList IList Curve )](475f2655-9de8-66d5-441a-63b1e001452f.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetHookOrientationAngle](Rebar-Free-Form-Accessor-Set-Hook-Orientation-Angle-Method.md) | **Obsolete.** Set the termination's rotation angle at end.  The angle will be used for both hook and crank.  Will throw exception if the rebar has valid constraints. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetHookPlaneNormalForBarIdx](Rebar-Free-Form-Accessor-Set-Hook-Plane-Normal-For-Bar-Idx-Method.md) | **Obsolete.** Set the plane's normal in which the termination at end of bar with index barPositionIndex will stay.  The plane's normal will be used for both hook and crank.  Will throw exception if the rebar has valid constraints. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsFixedNumber](18bde367-36cd-ed5b-33cc-9d908158be4a.htm) | Sets the Layout Rule property of rebar set to Fixed Number. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsMaximumSpacing](45957132-0208-54f9-c191-00ae98333a15.htm) | Sets the Layout Rule property of rebar set to Maximum Spacing. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsMinimumClearSpacing](9f22ba8b-df0c-31fe-14f4-62e1ee79a04f.htm) | Sets the Layout Rule property of rebar set to Minimum Clear Spacing. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsNumberWithSpacing](6ff04299-3217-c078-5f59-3f058c071bb2.htm) | Sets the Layout Rule property of rebar set to Number With Spacing. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsSingle](95e8c923-7dea-1bb2-e5b9-70974a46485f.htm) | Sets the Layout Rule property of rebar set to Single. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetReportedShape](Rebar-Free-Form-Accessor-Set-Reported-Shape-Method.md) | This method changes the RebarShape of a Free Form Rebar that is using RebarWorkInstructions.Straight property to the provided RebarShape. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetTerminationPlaneNormalForBarIndex](Rebar-Free-Form-Accessor-Set-Termination-Plane-Normal-For-Bar-Index-Method.md) | Sets the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay.  Will throw exception if the rebar has valid constraints. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Obtain an instance of this class from [GetFreeFormAccessor](67be446c-e2e1-9dfe-315f-f5d6adc779b9.htm) .
 The accessor includes a reference to the Rebar element.
 If the referenced Rebar element is deleted, using the methods form this class will throw exception. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
