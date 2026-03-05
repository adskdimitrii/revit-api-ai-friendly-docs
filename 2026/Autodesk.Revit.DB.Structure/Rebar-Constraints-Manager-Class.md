# Rebar Constraints Manager Class

Source: https://www.revitapidocs.com/2026/32fe1ec6-ddb3-feac-f18c-8683b054f639.htm

---

| Rebar Constraints Manager Class |
| --- |

A class used to obtain information about the constraints (RebarConstraint) acting
 on the shape handles (RebarConstrainedHandle) of a Rebar element, and modify the constraints. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure RebarConstraintsManager 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RebarConstraintsManager : IDisposable
```

```
Public Class RebarConstraintsManager
	Implements IDisposable
```

```
public ref class RebarConstraintsManager : IDisposable
```

```
type RebarConstraintsManager = 
    class
        interface IDisposable
    end
```
The RebarConstraintsManager type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsRebarConstrainedPlacementEnabled](57d251df-b6a9-6b12-a3c2-22be9245c205.htm) | A static property defining if the 'Rebar Constrained Placement' setting is on or off in current Revit Application Session. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](8a9d9f87-6f3f-40c9-578b-a2a5b6cb7311.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AllowConstraintTargets](1bfc99e7-7932-5a57-1f11-1d40ed940405.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ApplyRebarConstraints](ea70f469-13c9-8fea-a2f1-34796dc2c416.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearHandleConstraintPairHighlighting](5a96c36b-097c-0f79-1919-595c1aa7a351.htm) | Clears all highlighting in all views. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](ed88eaca-9e47-38a8-4515-b130810de0df.htm) | Releases all resources used by the RebarConstraintsManager |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAllConstrainedHandles](d87a1741-7965-413d-3c44-666516fd31aa.htm) | Retrieves all handles on the Rebar that are constrained to external references. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAllHandles](1a8dbc43-88f6-8087-1607-7b01d61f4560.htm) | Gets all RebarConstrainedHandles of this bar. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetConstraintCandidatesForHandle(RebarConstrainedHandle, ElementId)](7fb6f4f8-a01f-b6c5-e553-08197ef55db6.htm) | For shape driven rebar returns all possible RebarConstraints belonging to references from the provided element that could be used for a specified RebarConstrainedHandle. For free form rebar will return an empty list. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetConstraintCandidatesForHandle(RebarConstrainedHandle, Reference)](0639839a-a7a6-064d-5797-9ed609033b53.htm) | For shape driven rebar returns all possible RebarConstraints that will constrain RebarConstrainedHandle to the provided reference. For free form rebar will return an empty list. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCurrentConstraintOnHandle](6020571a-fa8f-5f21-3874-f808456a8854.htm) | Retrieves the RebarConstraint that acts on the specified RebarConstraintHandle. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPreferredConstraintOnHandle](4f92a917-683e-52f7-ad29-de2025af0220.htm) | For ShapeDriven: Returns the RebarConstraint that has been set as preferred for the specified RebarConstrainedHandle. For FreeForm: Returns the RebarConstraint that acts on the specified RebarConstraintHandle. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasValidRebar](6744e58e-e5ae-78ae-4183-1558827782b4.htm) | Checks whether the Manager's Rebar is still valid. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HighlightHandleConstraintPairInAllViews](4d33c054-d51a-f0a5-15a0-41625ca5e2a4.htm) | Highlights the specified RebarConstrainedHandle and RebarConstraint in all views. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemovePreferredConstraintFromHandle](9920f476-fcf4-0aa7-ec87-9c2975aed905.htm) | For ShapeDriven: Clears the user\-preferred RebarConstraint from the specified RebarConstrainedHandle. For FreeForm: Removes the RebarConstraint that is associated to the specified RebarConstrainedHandle. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetPreferredConstraint](b862c316-d105-8ff4-73aa-57ac354aea94.htm) | Sets the RebarConstraint as preferred constraint for its RebarConstrainedHandle. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetPreferredConstraintsToSurfaceForHandles](292c7344-279a-43f3-02a3-2db4ca676081.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A RebarConstraintsManager is created by calling Rebar.GetRebarConstraintsManager(),
 and can only be used to query or change constraints on the rebar element that
 created it. 

The constraint manager has different behavior, depending on the type of Rebar that created it:
 Shape Driven or FreeForm 

\-\-\-\-\-ShapeDriven\-\-\-\-\- 

If the Rebar is Shape Driven, Revit uses the following logic to choose automatic constraints
 for each handle on a rebar element. First, a search is performed to find all suitable target
 planes, including surfaces of the rebar's host, as well as surfaces on other
 concrete host elements that are attached to the rebar's host. In the case of
 standard style rebar, any host surface occupied by a stirrup will be ignored,
 and instead, the handles on the stirrup itself will be treated as candidates
 to form a constraint. 

Once all the constraint target candidates have been determined, the following
 sequence is used to select a constraint target: 

1. If the rebar is a straight standard bar, it will search the list of candidates
 for stirrup bends to lock its RebarPlane and Edge handles. If a bend is found within
 tolerance distance, then the bar will be snapped and constrained to that bend.
2. The bar will snap and constrain its handle to any host cover or stirrup handle
 that lies within tolerance distance.
3. If no candidate is found within tolerance, then the bar will choose nearest
 host surface target, with or without cover, and create an automatic constant distance
 constraint to that surface.

Snapping tolerances are 0\.5 \* bar diameter for host surface cover constraints and
 0\.5 \* (bar diameter \+ stirrup bar diameter) for stirrup handle constraints. 

The RebarConstraintsManager allows the API developer to obtain the constraint
 candidates for each constrained handle on a rebar, and to override the default
 target selection logic by setting a particular constraint as preferred.
 The API developer will be able to choose an automatic constraint, or can get
 constraint candidates to any host in the model or to any Rebar in the model no matter
 what style it is (Standard or Stirrup). There can be set constraints to generic surfaces as well.
 This can be useful in a number of ways. First, it can be used to snap a handle to a
 particular host surface or stirrup rebar handle, or to position a handle at a
 precise distance from a host surface. Second, it can force a rebar handle to
 constrain itself to a particular target surface, even if other targets are closer
 (or will become closer in subsequent updates of the Revit model). For example,
 a bar can be constrained to maintain a constant offset distance from a face of
 an opening in a slab, even if the opening is placed close to the edge of the slab
 and the bar would normally constrain itself to the slab edge. Lastly, the override
 can be used to cancel the default standard bar preference for stirrup bar handle
 planes, and to allow standard bars to be constrained to host cover surfaces, even
 when a stirrup is present. 

\-\-\-\-\- FreeForm \-\-\-\-\- 

If the rebar is FreeForm, then it requires input constraints that will be consumed to
 obtain the actual shape of the bar. The calculation method of the constraints passed
 to the rebar is custom made by an API application \- [IRebarUpdateServer](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm) . 

The RebarConstraintsManager can return all the possible "shape" handles
 and can set constraints created only with one of those handles.
 There are only active constraints on a FreeForm bar, the current and preferred notions
 represent the same thing. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
