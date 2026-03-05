# Linear Array Class

Source: https://www.revitapidocs.com/2026/58e47064-607e-d52b-5930-7e371851a678.htm

---

| Linear Array Class |
| --- |

An object that represents an Array created linearly within the Revit project. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB Element](Element-Class.md) 
[Autodesk.Revit.DB BaseArray](d7f9a542-0333-2e10-83a2-98afcee00b80.htm) 
Autodesk.Revit.DB LinearArray 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class LinearArray : BaseArray
```

```
Public Class LinearArray
	Inherits BaseArray
```

```
public ref class LinearArray : public BaseArray
```

```
type LinearArray = 
    class
        inherit BaseArray
    end
```
The LinearArray type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AssemblyInstanceId](83989f69-1aca-1a49-9647-e57bc2d58b21.htm) | The id of the assembly instance to which the element belongs. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BoundingBox](def2f9f2-b23a-bcea-43a3-e6de41b014c8.htm) | Retrieves a box that circumscribes all geometry of the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Category](8990bd36-af08-fc99-496b-f94fcb056b21.htm) | Retrieves a Category object that represents the category or sub category in which the element resides. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CreatedPhaseId](c6032e01-f7cb-b2ea-3312-697d14216a31.htm) | Id of a Phase at which the Element was created. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DemolishedPhaseId](7949a983-c5dc-62a3-594a-d685365449d5.htm) | Id of a Phase at which the Element was demolished. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DesignOption](5c20fe58-e301-6ddb-3438-666db5c586ee.htm) | Returns the design option to which the element belongs. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](9e530d25-61ca-3899-a531-cbcfd994358d.htm) | Returns the Document in which the Element resides. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Geometry](d8a55a5b-2a69-d5ab-3e1f-6cf1ee43c8ec.htm) | Retrieves the geometric representation of the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [GroupId](9508a6c5-9681-bbef-07c5-1351583b0e1e.htm) | The id of the group to which an element belongs. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Id](9235095b-b7ae-b6e5-6cc2-2b8d397644de.htm) | A unique identifier for an Element in an Autodesk Revit project. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsModifiable](65f9f835-daaa-3efa-2976-3f932aa18366.htm) | Identifies if the element is modifiable. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm) | Indicates whether an element is transient or permanent. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](0ffcf585-a39d-623c-9b5b-ab63c7bebfb6.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Label](816d60e1-d4ea-cda1-4736-aa5f7d05594a.htm) | The family parameter label of the BaseArray. (Inherited from [BaseArray](d7f9a542-0333-2e10-83a2-98afcee00b80.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LevelId](27033fe3-6740-61e3-be82-47a6b8ae77db.htm) | The id of the level associated with the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Location](89438f4f-7e15-835a-0c66-d6adbc8dd00c.htm) | This property is used to find the physical location of an element within a project. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Name](4eecb0d1-7633-86b7-d95c-42a4362f0b2c.htm) | Get and Set the Name property (Inherited from [BaseArray](d7f9a542-0333-2e10-83a2-98afcee00b80.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [NumMembers](f2ed4299-f623-dc05-6e95-f3bfd234d9ae.htm) | Retrieves or changes the number of arrayed members. Array placeholder members in the family environment are not counted. (Overrides [BaseArray NumMembers](66183f2d-7dee-631d-3dcb-0d484d134c91.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm) | The id of the view that owns the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter BuiltInParameter](2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.htm) | Retrieves a parameter from the element given a parameter id. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter Definition](87d8a88c-906e-85a9-f575-f263788b8584.htm) | Retrieves a parameter from the element based on its definition. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm) | Retrieves a parameter from the element given a GUID for a shared parameter. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameters](7af5d66f-4533-33d2-dd82-d9573eaabf15.htm) | Retrieves a set containing all of the parameters that are contained within the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ParametersMap](82c45482-a018-32e4-d8e5-9751e10ffeb9.htm) | Retrieves a map containing all of the parameters that are contained within the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Pinned](c37bc7f9-409e-9b8a-f491-f700228985e2.htm) | Identifies if the element has been pinned to prevent changes. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm) | A stable unique identifier for an element within the document. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VersionGuid](2a1eae53-2c5c-a7be-1ef2-0f48626c62f5.htm) | Get the element version Guid. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ViewSpecific](785b351e-51cb-e3c6-cb91-f307c8e4ba73.htm) | Identifies if the element is owned by a view. (Inherited from [Element](Element-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [WorksetId](4b45250a-7a07-a89a-0f63-cf8d142a7b93.htm) | Get Id of the Workset which owns the element. (Inherited from [Element](Element-Class.md) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ArrayElementsWithoutAssociation](5c97b79a-6d6b-5f74-fa3f-c35fbc96d01c.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ArrayElementWithoutAssociation](260ee73e-2196-79a3-19ac-f942aafc44f4.htm) | Creates a new linear array from a single element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.htm) | Indicates if the element can be hidden in the view. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.htm) | Identifies if the element can be locked. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.htm) | Checks if given subelement can be removed from the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanHaveTypeAssigned](051e2945-b690-5387-d083-7cdb7cb75332.htm) | Identifies if the element can have a type assigned. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.htm) | Changes the type of the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create(Document, View, ElementId, Int32, XYZ, ArrayAnchorMember)](33520964-cb76-56b5-a303-bd2bad01adfe.htm) | Creates a new linear array element from a single element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create(Document, View, ICollection ElementId , Int32, XYZ, ArrayAnchorMember)](77e8c92f-6b48-0f3d-923c-2737a6d6e4ab.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.htm) | Deletes the existing entity created by %schema% in the element (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.htm) | Removes a subelement from the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.htm) | (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.htm) | (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [EvaluateAllParameterValues](5250da77-1e16-13c6-fed6-5ef29997e6f9.htm) | Evaluates all the parameters' values of the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [EvaluateParameterValues](1a6ca65f-09d9-a4e6-9365-3ed64e3097fc.htm) | (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCopiedMemberIds](1d424df0-983c-4ebd-b749-6bec157e30b5.htm) | Retrieves the copied member ids from the array. The first item in an array contains the original elements from which the array was created. All other items in the array are copies. (Overrides [BaseArray GetCopiedMemberIds](ce0d8197-a99f-0ef2-32a8-51d4cc2aa101.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.htm) | Get all elements that, from a logical point of view, are the children of this Element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.htm) | Returns the existing entity corresponding to the Schema if it has been saved in the  Element, or an invalid entity otherwise. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.htm) | Returns the Schema guids of any Entities stored in this element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.htm) | Gets information pertaining to the external file referenced  by the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.htm) | Gets the ExternalResourceReference associated with a specified external resource type. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.htm) | Gets the collection of ExternalResourceReference associated with a specified external resource type. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.htm) | Gets the map of the external resource references referenced  by the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.htm) | Gets the expanded map of the external resource references referenced  by the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.htm) | Returns the ids of the element(s) that generated the input geometry object. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.htm) | Retrieve one geometric primitive contained in the element given a reference. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.htm) | Gets the area of the material with the given id. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.htm) | Gets the element ids of all materials present in the element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.htm) | Gets the volume of the material with the given id. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetMinimumSize](f90fe0c3-22c2-baee-a122-6958cc50c914.htm) | Returns the minimum size for a linear array based on the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.htm) | Provides the link instance IDs when the element is monitoring. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.htm) | Provides the local element IDs when the element is monitoring. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfMembersIncludingPlaceholders](a8947a57-af78-20b3-abac-421fb9e2ca04.htm) | Returns the number of items in an array, including placeholder items in families. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.htm) | Gets the parameters associated to the element in order. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOriginalMemberIds](99315d93-cf2a-8619-49de-0864a5b742cc.htm) | Retrieves the ids for the original elements from which the array was created. These elements form the first item in the array. (Overrides [BaseArray GetOriginalMemberIds](8c15fb58-a534-abd4-0715-841ea1c1447f.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.htm) | Retrieves a parameter from the element given identifier. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.htm) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.htm) | Retrieves the parameters from the element via the given name. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.htm) | Gets the status of a given element in the input phase (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm) | Returns the collection of element subelements. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.htm) | Returns the identifier of this element's type. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetValidTypes](086554ba-3c70-9c0f-8a09-55a4da4ef905.htm) | Obtains a set of types that are valid for this element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.htm) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsElementArrayable](c7a9d13d-f660-659d-732b-13718d298e8a.htm) | Indicates whether the input element is arrayable. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.htm) | Determines whether this Element represents an external  file. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm) | Identifies if the element has been permanently hidden in the view. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.htm) | Indicate whether an element is monitoring any elements in any linked models. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.htm) | Indicate whether an element is monitoring other local elements. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.htm) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.htm) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsValidNumberOfMembers](a1f0d0cf-b0e0-a110-5d9f-d747f6761c92.htm) | This indicates whether the input count is a valid size for an array based on the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.htm) | Checks if given type is valid for this element. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.htm) | Attempts to find a parameter on the element which has the given name. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.htm) | Determines whether this Element uses external resources associated with  a specified external resource type. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.htm) | Determines whether this Element uses external resources. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.htm) | Stores the entity in the element. If an Entity described by the same Schema already  exists, it is overwritten. (Inherited from [Element](Element-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
