# Rebar Container Item Class

Source: https://www.revitapidocs.com/2026/764f647c-9c3e-b971-1c44-b63f756e1448.htm

---

| Rebar Container Item Class |
| --- |

Provides implementation for Rebar stored in RebarContainer. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarContainerItem 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarContainerItem : IDisposable
```

```
Public Class RebarContainerItem
	Implements IDisposable
```

```
public ref class RebarContainerItem : IDisposable
```

```
type RebarContainerItem = 
    class
        interface IDisposable
    end
```
The RebarContainerItem type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ArrayLength](65bd5b22-0211-e66c-18e9-72798ce675d5.htm) | Identifies the distribution path length of rebar set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BarsOnNormalSide](9ad847b0-7284-8d68-d56a-46b916445b2e.htm) | Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BarTypeId](e01fc1b7-7414-ee88-44b5-91ece090d12e.htm) | The identifier of the rebar bar type. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BaseFinishingTurns](db8f7048-da0b-878e-6eae-d1cb4c193f4e.htm) | For a spiral, the number of finishing turns at the lower end of the spiral. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Height](5e8dda08-99a3-3086-20eb-30aed04c08a8.htm) | For a spiral, the overall height. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IncludeFirstBar](45834539-61e2-aeba-fd24-d4acd5487ac8.htm) | Identifies if the first bar in rebar set is shown. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IncludeLastBar](a4a23934-9f45-e5a9-6352-752f8595619b.htm) | Identifies if the last bar in rebar set is shown. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](bb1de878-6485-5c21-73f8-da9296e510fa.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ItemIndex](26ff332f-e5c0-a69a-63b1-c49d309d9b18.htm) | The index of this item in its associated RebarContainer. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LayoutRule](3bf12e22-a943-c022-51ac-4cd62099dc94.htm) | Identifies the layout rule of rebar set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MaxSpacing](d750a266-d22b-c73e-2622-a32147f0a39c.htm) | Identifies the maximum spacing between rebar in rebar set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MultiplanarDepth](6a44a37f-c914-9bcb-bcc8-18df3e69f159.htm) | For a multiplanar rebar, the depth of the instance. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Normal](6dc405d3-b991-42e7-b2b6-b8e00ac71908.htm) | A unit\-length vector normal to the plane of the rebar |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [NumberOfBarPositions](ed0dc2dd-b3eb-4f4d-75d0-e9d75cea444e.htm) | The number of potential bars in the set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Pitch](e76fccf0-1b96-9732-6fcc-b1c3399c1b27.htm) | For a spiral, the pitch, or vertical distance traveled in one rotation. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Quantity](5e0196f4-e72f-c940-9d51-eda1456b55d5.htm) | Identifies the number of bars in rebar set. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RebarShapeId](Rebar-Container-Item-Rebar-Shape-Id-Property.md) | The RebarShape element that defines the shape of the rebar. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TopFinishingTurns](48be1e27-574c-6cba-1b98-c024823d301e.htm) | For a spiral, the number of finishing turns at the upper end of the spiral. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TotalLength](9c3cc4f9-47b9-994c-a8b6-a06524558daf.htm) | The length of an individual bar multiplied by Quantity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Volume](d42b0a63-b2a5-4657-09a9-cfe39736e2fb.htm) | The volume of an individual bar multiplied by Quantity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanApplyPresentationMode](b5e087e1-791d-2410-5c71-39a231e5bb32.htm) | Checks if a presentation mode can be applied for this rebar in the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanUseHookType](1a969227-e826-316a-7cef-a0d2beb2b948.htm) | Checks if the specified RebarHookType id is of a valid RebarHookType for the Rebar's RebarBarType |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearPresentationMode](b23d7436-582b-d552-4876-457a83b31640.htm) | Sets the presentation mode for this rebar set to the default (either for a single view, or for all views). |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ComputeDrivingCurves](b2c67a47-1b2d-ed45-eb9a-8b88087d0cfb.htm) | Compute the driving curves. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](f2e214b9-dd55-bcd9-877b-e24771ca3f4c.htm) | Releases all resources used by the RebarContainerItem |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DoesBarExistAtPosition](ff2cf48e-9017-c8ad-c217-9466bfd34e22.htm) | Checks whether a bar exists at the specified position. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [FindMatchingPredefinedPresentationMode](c6425365-afc4-b069-d5f4-6e6c773a6a2b.htm) | Determines if there is a matching RebarPresentationMode for the current set of selected hidden and unhidden bars assigned to the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetBarPositionTransform](b04c00e0-b32c-428e-0217-65a0958a6308.htm) | Return a transform representing the relative position of any  individual bar in the set. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetBendData](0b86dcae-5f5f-5cf4-f5f3-4d8bbf33f27c.htm) | Gets the RebarBendData, containing bar and hook information, of the instance. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCenterlineCurves(Boolean, Boolean, Boolean)](ddd3caf7-9e00-4137-805f-33ef21a13f8f.htm) | A chain of curves representing the centerline of the rebar. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCenterlineCurves(Boolean, Boolean, Boolean, MultiplanarOption)](e82968e2-d333-95be-1d24-c45cdac94520.htm) | A chain of curves representing the centerline of the rebar. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDistributionPath](0a43e43f-fc15-d257-b159-dc76aedc2743.htm) | The distribution path of a rebar set. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookOrientation](Rebar-Container-Item-Get-Hook-Orientation-Method.md) | **Obsolete.** Returns the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHookTypeId](96c3c52f-1d5a-f8a8-ce56-867a3fa38110.htm) | Get the id of the RebarHookType to be applied to the rebar. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPresentationMode](738e3080-7657-2dc7-6dd4-5827c9ea718d.htm) | Gets the presentaion mode for this rebar set when displayed in the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTerminationOrientation](Rebar-Container-Item-Get-Termination-Orientation-Method.md) | Gets the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasPresentationOverrides](abc20bda-3702-2099-e137-7ce85fdf1676.htm) | Identifies if this rebar set has overridden default presentation settings for the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsBarHidden](93adc3a0-aa5e-c492-10d8-c9b6442659d0.htm) | Identifies if a given bar in this rebar set is hidden in this view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsRebarInSection](8ba6812e-6cbf-1383-48e0-02630d3b1e6c.htm) | Identifies if this rebar set is shown as a cross\-section in the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetBarHiddenStatus](0310106a-d8a1-0dd9-fcbe-272b7e231d52.htm) | Sets the bar in this rebar set to be hidden or unhidden in the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromCurves(RebarStyle, RebarBarType, RebarHookType, RebarHookType, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation, Boolean, Boolean)](Rebar-Container-Item-Set-From-Curves-Rebar-Style-Rebar-Bar-Type-Rebar-Hook-Type-Rebar-Hook-Type-XYZ-IList-Curve-Rebar-Hook-Orientation-Rebar-Hook-Orientation-Boolean-Boolean-Method.md) | **Obsolete.** |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromCurves(RebarStyle, RebarBarType, RebarHookType, RebarHookType, XYZ, IList Curve , RebarTerminationOrientation, RebarTerminationOrientation, Boolean, Boolean)](Rebar-Container-Item-Set-From-Curves-Rebar-Style-Rebar-Bar-Type-Rebar-Hook-Type-Rebar-Hook-Type-XYZ-IList-Curve-Rebar-Termination-Orientation-Rebar-Termination-Orientation-Boolean-Boolean-Method.md) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromCurvesAndShape(RebarShape, RebarBarType, RebarHookType, RebarHookType, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation)](Rebar-Container-Item-Set-From-Curves-And-Shape-Rebar-Shape-Rebar-Bar-Type-Rebar-Hook-Type-Rebar-Hook-Type-XYZ-IList-Curve-Rebar-Hook-Orientation-Rebar-Hook-Orientation-Method.md) | **Obsolete.** |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromCurvesAndShape(RebarShape, RebarBarType, RebarHookType, RebarHookType, XYZ, IList Curve , RebarTerminationOrientation, RebarTerminationOrientation)](Rebar-Container-Item-Set-From-Curves-And-Shape-Rebar-Shape-Rebar-Bar-Type-Rebar-Hook-Type-Rebar-Hook-Type-XYZ-IList-Curve-Rebar-Termination-Orientation-Rebar-Termination-Orientation-Method.md) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromRebar](Rebar-Container-Item-Set-From-Rebar-Method.md) | Set an instance of a RebarContainerItem element according to a Rebar parameters.  Will throw exception if given rebar is not shape driven.  Will throw exception if given rebar has moved bars in set. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFromRebarShape](Rebar-Container-Item-Set-From-Rebar-Shape-Method.md) | Set an instance of a RebarContainerItem element, as an instance of a RebarShape.  The instance will have the default shape parameters from the RebarShape,  and its location is based on the bounding box of the shape in the shape definition.  Hooks are removed from the shape before computing its bounding box.  If appropriate hooks can be found in the document, they will be assigned arbitrarily. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetHookOrientation](Rebar-Container-Item-Set-Hook-Orientation-Method.md) | **Obsolete.** Sets the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetHookTypeId](9aef5675-a0b7-de1c-01e1-19b8566c79b3.htm) | Set the id of the RebarHookType to be applied to the rebar. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsFixedNumber](7c171f9c-694b-ca7f-9666-d468e51493b9.htm) | Sets the Layout Rule property of rebar set to FixedNumber. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsMaximumSpacing](d88219dd-f484-4738-5c1d-46a676fac072.htm) | Sets the Layout Rule property of rebar set to MaximumSpacing |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsMinimumClearSpacing](7f8cfdd8-6203-b0f6-da80-6539e01244eb.htm) | Sets the Layout Rule property of rebar set to MinimumClearSpacing |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsNumberWithSpacing](f081a636-988a-4b34-927a-6fdaf1792404.htm) | Sets the Layout Rule property of rebar set to NumberWithSpacing |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayoutAsSingle](d0cb300b-c097-dc81-f296-8285261bfdc0.htm) | Sets the Layout Rule property of rebar set to Single. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetPresentationMode](686fc4e7-a053-fafd-affe-61b6018e9634.htm) | Sets the presentation mode for this rebar set when displayed in the given view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetTerminationOrientation](Rebar-Container-Item-Set-Termination-Orientation-Method.md) | Defines the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
