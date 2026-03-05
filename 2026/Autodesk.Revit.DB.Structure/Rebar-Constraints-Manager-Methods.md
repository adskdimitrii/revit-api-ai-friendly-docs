# Rebar Constraints Manager Methods

Source: https://www.revitapidocs.com/2026/c0ea35cf-f8da-bee5-9264-82473ed37d0c.htm

---

| Rebar Constraints Manager Methods |
| --- |

The [RebarConstraintsManager](Rebar-Constraints-Manager-Class.md) type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AllowConstraintTargets](1bfc99e7-7932-5a57-1f11-1d40ed940405.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ApplyRebarConstraints](ea70f469-13c9-8fea-a2f1-34796dc2c416.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearHandleConstraintPairHighlighting](5a96c36b-097c-0f79-1919-595c1aa7a351.htm) | Clears all highlighting in all views. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](ed88eaca-9e47-38a8-4515-b130810de0df.htm) |  |
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

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarConstraintsManager Class](Rebar-Constraints-Manager-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
