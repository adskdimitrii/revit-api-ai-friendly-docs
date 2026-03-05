# Element Class

Source: https://www.revitapidocs.com/2026/eb16114f-69ea-f4de-0d0d-f7388b105a16.htm

---

| Element Class |
| --- |

Base class for most persistent data within a Revit document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB Element 
[More](#fullInheritance) 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class Element : IDisposable
```

```
Public Class Element
	Implements IDisposable
```

```
public ref class Element : IDisposable
```

```
type Element = 
    class
        interface IDisposable
    end
```
The Element type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AssemblyInstanceId](83989f69-1aca-1a49-9647-e57bc2d58b21.htm) | The id of the assembly instance to which the element belongs. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BoundingBox](def2f9f2-b23a-bcea-43a3-e6de41b014c8.htm) | Retrieves a box that circumscribes all geometry of the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Category](8990bd36-af08-fc99-496b-f94fcb056b21.htm) | Retrieves a Category object that represents the category or sub category in which the element resides. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CreatedPhaseId](c6032e01-f7cb-b2ea-3312-697d14216a31.htm) | Id of a Phase at which the Element was created. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DemolishedPhaseId](7949a983-c5dc-62a3-594a-d685365449d5.htm) | Id of a Phase at which the Element was demolished. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DesignOption](5c20fe58-e301-6ddb-3438-666db5c586ee.htm) | Returns the design option to which the element belongs. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](9e530d25-61ca-3899-a531-cbcfd994358d.htm) | Returns the Document in which the Element resides. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Geometry](d8a55a5b-2a69-d5ab-3e1f-6cf1ee43c8ec.htm) | Retrieves the geometric representation of the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [GroupId](9508a6c5-9681-bbef-07c5-1351583b0e1e.htm) | The id of the group to which an element belongs. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Id](9235095b-b7ae-b6e5-6cc2-2b8d397644de.htm) | A unique identifier for an Element in an Autodesk Revit project. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsModifiable](65f9f835-daaa-3efa-2976-3f932aa18366.htm) | Identifies if the element is modifiable. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm) | Indicates whether an element is transient or permanent. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](0ffcf585-a39d-623c-9b5b-ab63c7bebfb6.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LevelId](27033fe3-6740-61e3-be82-47a6b8ae77db.htm) | The id of the level associated with the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Location](89438f4f-7e15-835a-0c66-d6adbc8dd00c.htm) | This property is used to find the physical location of an element within a project. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Name](e372092e-ff47-71c2-1272-50ab08e5a41d.htm) | A human readable name for the Element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm) | The id of the view that owns the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter BuiltInParameter](2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.htm) | Retrieves a parameter from the element given a parameter id. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter Definition](87d8a88c-906e-85a9-f575-f263788b8584.htm) | Retrieves a parameter from the element based on its definition. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm) | Retrieves a parameter from the element given a GUID for a shared parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Parameters](7af5d66f-4533-33d2-dd82-d9573eaabf15.htm) | Retrieves a set containing all of the parameters that are contained within the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ParametersMap](82c45482-a018-32e4-d8e5-9751e10ffeb9.htm) | Retrieves a map containing all of the parameters that are contained within the element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Pinned](c37bc7f9-409e-9b8a-f491-f700228985e2.htm) | Identifies if the element has been pinned to prevent changes. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm) | A stable unique identifier for an element within the document. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VersionGuid](2a1eae53-2c5c-a7be-1ef2-0f48626c62f5.htm) | Get the element version Guid. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ViewSpecific](785b351e-51cb-e3c6-cb91-f307c8e4ba73.htm) | Identifies if the element is owned by a view. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [WorksetId](4b45250a-7a07-a89a-0f63-cf8d142a7b93.htm) | Get Id of the Workset which owns the element. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.htm) | Indicates if the element can be hidden in the view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.htm) | Identifies if the element can be locked. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.htm) | Checks if given subelement can be removed from the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanHaveTypeAssigned](051e2945-b690-5387-d083-7cdb7cb75332.htm) | Identifies if the element can have a type assigned. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CanHaveTypeAssigned(Document, ICollection ElementId )](3cfda085-5bba-a1d2-1a40-0f2872a6ef22.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.htm) | Changes the type of the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ChangeTypeId(Document, ICollection ElementId , ElementId)](6026a054-5e1e-5cac-7283-aa102aa997e3.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.htm) | Deletes the existing entity created by %schema% in the element |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.htm) | Removes a subelement from the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.htm) | Releases all resources used by the Element |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [EvaluateAllParameterValues](5250da77-1e16-13c6-fed6-5ef29997e6f9.htm) | Evaluates all the parameters' values of the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [EvaluateParameterValues](1a6ca65f-09d9-a4e6-9365-3ed64e3097fc.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeAny](e9a0bce4-b289-1ea1-05d0-c0fc2943f8dd.htm) | Returns ChangeType associated with any change in an element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeElementAddition](9f7a0758-21b5-bba6-5d26-9e1f40d29f7f.htm) | Returns ChangeType associated with element addition |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeElementDeletion](d2f0d0dd-d01b-3296-8248-068baec486cf.htm) | Returns ChangeType associated with element deletion. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeGeometry](45751c5b-6d10-657a-a017-04219d1a5ac8.htm) | Returns ChangeType associated with a change in the geometry of an element |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeParameter(ElementId)](6b0460f6-8db3-970c-d2d9-a1b5e470eb1e.htm) | Returns ChangeType associated with a change in a parameter's value |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetChangeTypeParameter(Parameter)](19ee7026-0e04-5bd2-b046-b14b59d4bc4e.htm) | Returns ChangeType associated with a change in a parameter's value |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.htm) | Get all elements that, from a logical point of view, are the children of this Element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.htm) | Returns the existing entity corresponding to the Schema if it has been saved in the  Element, or an invalid entity otherwise. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.htm) | Returns the Schema guids of any Entities stored in this element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.htm) | Gets information pertaining to the external file referenced  by the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.htm) | Gets the ExternalResourceReference associated with a specified external resource type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.htm) | Gets the collection of ExternalResourceReference associated with a specified external resource type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.htm) | Gets the map of the external resource references referenced  by the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.htm) | Gets the expanded map of the external resource references referenced  by the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.htm) | Returns the ids of the element(s) that generated the input geometry object. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.htm) | Retrieve one geometric primitive contained in the element given a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.htm) | Gets the area of the material with the given id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.htm) | Gets the element ids of all materials present in the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.htm) | Gets the volume of the material with the given id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.htm) | Provides the link instance IDs when the element is monitoring. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.htm) | Provides the local element IDs when the element is monitoring. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.htm) | Gets the parameters associated to the element in order. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.htm) | Retrieves a parameter from the element given identifier. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.htm) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.htm) | Retrieves the parameters from the element via the given name. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.htm) | Gets the status of a given element in the input phase |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm) | Returns the collection of element subelements. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.htm) | Returns the identifier of this element's type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetValidTypes](086554ba-3c70-9c0f-8a09-55a4da4ef905.htm) | Obtains a set of types that are valid for this element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetValidTypes(Document, ICollection ElementId )](43dc2992-0b0d-ca73-d63c-2ac829bf1a89.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.htm) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.htm) | Determines whether this Element represents an external  file. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm) | Identifies if the element has been permanently hidden in the view. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.htm) | Indicate whether an element is monitoring any elements in any linked models. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.htm) | Indicate whether an element is monitoring other local elements. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.htm) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.htm) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.htm) | Checks if given type is valid for this element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsValidType(Document, ICollection ElementId , ElementId)](dec7e1c1-c16b-f159-7e56-6e654a5110e2.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.htm) | Attempts to find a parameter on the element which has the given name. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.htm) | Determines whether this Element uses external resources associated with  a specified external resource type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.htm) | Determines whether this Element uses external resources. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.htm) | Stores the entity in the element. If an Entity described by the same Schema already  exists, it is overwritten. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The data in a Revit document consists primarily of a collection of
 elements. An element usually corresponds to a single component of a
 building or drawing, such as a wall, door, or dimension, but it can
 also be something more abstract, like a wall type or a view.
 Every element in a document has a unique ID, represented by the
 ElementId class. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB Element 
[Autodesk.Revit.DB.Analysis AnalysisDisplayLegend](c9bd55c9-e4fc-8a7a-0cd9-b2605fcb6a56.htm) 
[Autodesk.Revit.DB.Analysis AnalysisDisplayStyle](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm) 
[Autodesk.Revit.DB.Analysis BuildingOperatingDaySchedule](b9a7693c-e3ae-72d0-8d15-b377025b90b7.htm) 
[Autodesk.Revit.DB.Analysis BuildingOperatingYearSchedule](18d6fc71-5801-04cf-082d-4deb26b7756b.htm) 
[Autodesk.Revit.DB.Analysis ConceptualSurfaceType](b79ddf97-2888-ceda-a2c4-222dab08163e.htm) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisConstruction](81de66b3-0235-9d05-14ee-22bf2efac937.htm) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisDetailModel](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisMaterial](a02470b1-6055-c4f1-875d-d612ca28c4f2.htm) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisOpening](../Autodesk.Revit.DB.Analysis/Energy-Analysis-Opening-Class.md) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisSpace](../Autodesk.Revit.DB.Analysis/Energy-Analysis-Space-Class.md) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisSurface](../Autodesk.Revit.DB.Analysis/Energy-Analysis-Surface-Class.md) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisWindowType](111f4f79-f802-7add-41c0-e51e062ed832.htm) 
[Autodesk.Revit.DB.Analysis EnergyAnalysisZone](../Autodesk.Revit.DB.Analysis/Energy-Analysis-Zone-Class.md) 
[Autodesk.Revit.DB.Analysis EnergyDataSettings](../Autodesk.Revit.DB.Analysis/Energy-Data-Settings-Class.md) 
[Autodesk.Revit.DB.Analysis GenericZone](../Autodesk.Revit.DB.Analysis/Generic-Zone-Class.md) 
[Autodesk.Revit.DB.Analysis HVACLoadType](90bf5784-0076-ded0-41fb-38fcb8ed6abe.htm) 
[Autodesk.Revit.DB.Analysis MassLevelData](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.htm) 
[Autodesk.Revit.DB.Analysis MassSurfaceData](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm) 
[Autodesk.Revit.DB.Analysis PathOfTravel](99c2bb04-151f-c325-84b2-40dee81447d6.htm) 
[Autodesk.Revit.DB.Analysis RouteAnalysisSettings](e6742b6a-9c35-5344-736b-7bf9af6f4254.htm) 
[Autodesk.Revit.DB.Analysis SpatialFieldManager](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm) 
[Autodesk.Revit.DB AppearanceAssetElement](3493da3a-fea5-69cb-a18e-d0a954615bab.htm) 
[Autodesk.Revit.DB.Architecture ContinuousRail](253602af-6809-a579-fc2c-975888d5748c.htm) 
[Autodesk.Revit.DB.Architecture MultistoryStairs](8b07cbff-013c-889f-8807-703e63a91923.htm) 
[Autodesk.Revit.DB.Architecture Railing](4af1265f-859e-123b-ada5-a479324f3dee.htm) 
[Autodesk.Revit.DB.Architecture Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.htm) 
[Autodesk.Revit.DB.Architecture StairsLanding](cae109cd-bc50-6c36-300e-35d3457c0982.htm) 
[Autodesk.Revit.DB.Architecture StairsPath](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm) 
[Autodesk.Revit.DB.Architecture StairsRun](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm) 
[Autodesk.Revit.DB.Architecture TopographySurface](64242f41-69e1-84be-f21b-84783e81364a.htm) 
[Autodesk.Revit.DB AreaScheme](9b5fd895-692c-5b6f-87f9-e53b1cc7c163.htm) 
[Autodesk.Revit.DB AreaVolumeSettings](6282b3c9-3717-5c8f-7501-8a282244ce09.htm) 
[Autodesk.Revit.DB AssemblyInstance](4e60704c-dfe3-72b6-7892-6440503fa078.htm) 
[Autodesk.Revit.DB BaseArray](d7f9a542-0333-2e10-83a2-98afcee00b80.htm) 
[Autodesk.Revit.DB BasePoint](154074ae-d653-aaff-b84b-6336a1cbafaa.htm) 
[Autodesk.Revit.DB BeamSystem](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm) 
[Autodesk.Revit.DB ColorFillLegend](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm) 
[Autodesk.Revit.DB ColorFillScheme](Color-Fill-Scheme-Class.md) 
[Autodesk.Revit.DB CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.htm) 
[Autodesk.Revit.DB ComponentRepeater](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm) 
[Autodesk.Revit.DB ComponentRepeaterSlot](395d3527-1315-038e-8a47-80920f063cc6.htm) 
[Autodesk.Revit.DB ConnectorElement](cd7d7579-1058-e8ca-d55a-c3a914843667.htm) 
[Autodesk.Revit.DB Control](d04da6b9-0586-22b8-df13-8eb7f5ca248f.htm) 
[Autodesk.Revit.DB CurveElement](61673852-2d08-003d-e9fd-4be89d533774.htm) 
[Autodesk.Revit.DB DatumPlane](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm) 
[Autodesk.Revit.DB DefaultDivideSettings](c4d57a70-3192-458c-faa7-619d11c69f60.htm) 
[Autodesk.Revit.DB DesignOption](Design-Option-Class.md) 
[Autodesk.Revit.DB Dimension](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm) 
[Autodesk.Revit.DB DirectShape](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm) 
[Autodesk.Revit.DB DisplacementElement](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm) 
[Autodesk.Revit.DB DisplacementPath](90ac4bbb-7f65-763a-bf5e-a76b2a167294.htm) 
[Autodesk.Revit.DB DividedPath](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm) 
[Autodesk.Revit.DB DividedSurface](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm) 
[Autodesk.Revit.DB.Electrical AreaBasedLoadType](2800f280-409f-083d-5b57-127a19344de9.htm) 
[Autodesk.Revit.DB.Electrical CableTrayConduitRunBase](6820d2a3-d692-2d8e-cb69-d42060ace467.htm) 
[Autodesk.Revit.DB.Electrical CableTraySettings](99e3b914-6cf3-a0af-4c25-dc77048091f7.htm) 
[Autodesk.Revit.DB.Electrical CableTraySizes](dbd6f408-fbae-1fe0-0e61-7d611141d6b5.htm) 
[Autodesk.Revit.DB.Electrical CircuitNamingScheme](99de5fb2-6e65-7b1f-1866-347c40d427af.htm) 
[Autodesk.Revit.DB.Electrical CircuitNamingSchemeSettings](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm) 
[Autodesk.Revit.DB.Electrical ConduitSettings](c86a1700-e477-3888-7647-3eafa528fe5d.htm) 
[Autodesk.Revit.DB.Electrical ConduitSizeSettings](d385e4b4-f675-9bcc-d067-5ca7d1d000d4.htm) 
[Autodesk.Revit.DB.Electrical ElectricalAnalyticalLoadSet](04782b5e-7089-9825-459b-df47a45a0e71.htm) 
[Autodesk.Revit.DB.Electrical ElectricalAnalyticalNode](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm) 
[Autodesk.Revit.DB.Electrical ElectricalDemandFactorDefinition](8ad48bcf-05f3-b9c3-ebfb-2a7b2db2fd83.htm) 
[Autodesk.Revit.DB.Electrical ElectricalLoadClassification](c8aeb888-f4dd-4b93-063e-6aa118c0e471.htm) 
[Autodesk.Revit.DB.Electrical ElectricalSetting](../Autodesk.Revit.DB.Electrical/Electrical-Setting-Class.md) 
[Autodesk.Revit.DB.Electrical PanelScheduleSheetInstance](1fdb4d7e-ff99-78f7-8efa-87968f5defce.htm) 
[Autodesk.Revit.DB.Electrical PanelScheduleTemplate](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm) 
[Autodesk.Revit.DB ElementType](Element-Type-Class.md) 
[Autodesk.Revit.DB ElevationMarker](ca59d2f7-4cd0-d13d-22a0-c153ac8310d4.htm) 
[Autodesk.Revit.DB ExportDGNSettings](3df10700-a305-dba7-fc4a-5afb5387256c.htm) 
[Autodesk.Revit.DB ExportDWGSettings](a17fc52f-f67a-9763-e52f-29f867106908.htm) 
[Autodesk.Revit.DB ExportPDFSettings](66156539-3f22-d986-ea46-49e772d1c451.htm) 
[Autodesk.Revit.DB.ExtensibleStorage DataStorage](015081b6-3a45-1b4c-991a-93419e9acd51.htm) 
[Autodesk.Revit.DB FabricationConfiguration](f7094105-2acf-03f1-7a7f-82dd24087a17.htm) 
[Autodesk.Revit.DB FabricationPart](Fabrication-Part-Class.md) 
[Autodesk.Revit.DB FabricationServiceSettings](74134cf4-2874-3b29-5e0f-b4cd7b852ae9.htm) 
[Autodesk.Revit.DB FaceSplitter](ba55587f-4f1e-7f4c-5b1c-864e10cab304.htm) 
[Autodesk.Revit.DB Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm) 
[Autodesk.Revit.DB FilledRegion](3685651c-a789-3550-f6bb-7c1decc29079.htm) 
[Autodesk.Revit.DB FillPatternElement](64ecefd0-f5c4-5cd9-53bd-10a64739257e.htm) 
[Autodesk.Revit.DB FilterElement](909615cd-8abd-044a-cff2-f21fd95b8ee7.htm) 
[Autodesk.Revit.DB GraphicsStyle](da26fe81-ee66-1036-1f5b-dffe612182d9.htm) 
[Autodesk.Revit.DB Group](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm) 
[Autodesk.Revit.DB HostObject](56a32e0b-df65-a6ba-40bd-8f50a1f31dcd.htm) 
[Autodesk.Revit.DB IFCCategoryTemplate](IFCCategory-Template-Class.md) 
[Autodesk.Revit.DB IFCParameterTemplate](IFCParameter-Template-Class.md) 
[Autodesk.Revit.DB ImageInstance](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm) 
[Autodesk.Revit.DB IndependentTag](Independent-Tag-Class.md) 
[Autodesk.Revit.DB Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.htm) 
[Autodesk.Revit.DB InternalOrigin](61a029d2-81db-72c9-8fe6-f83d0aa0c658.htm) 
[Autodesk.Revit.DB KeyBasedTreeEntryTable](c5d3e9d9-0221-520b-6163-9843db20d5ea.htm) 
[Autodesk.Revit.DB LinePatternElement](8f4678ba-1824-fd00-73b6-dfb9c7802f83.htm) 
[Autodesk.Revit.DB Material](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm) 
[Autodesk.Revit.DB.Mechanical DuctSettings](../Autodesk.Revit.DB.Mechanical/Duct-Settings-Class.md) 
[Autodesk.Revit.DB.Mechanical DuctSizeSettings](68c1d227-424d-36da-0e5a-3f3e51e7f939.htm) 
[Autodesk.Revit.DB.Mechanical MechanicalEquipmentSet](ce3c8e90-566c-bb8e-57f7-06f10dac5b7c.htm) 
[Autodesk.Revit.DB.Mechanical MEPAnalyticalSystem](159ecf0e-1c10-84b1-72b8-104a414b76ed.htm) 
[Autodesk.Revit.DB.Mechanical MEPHiddenLineSettings](36aa6fd1-8948-f89d-3206-8bba2c3db54c.htm) 
[Autodesk.Revit.DB.Mechanical Zone](../Autodesk.Revit.DB.Mechanical/Zone-Class.md) 
[Autodesk.Revit.DB.Mechanical ZoneEquipment](62330781-b72c-02ae-0c30-c557decfc38a.htm) 
[Autodesk.Revit.DB MEPSystem](65946955-8638-fafb-2657-ef7cb7b2941b.htm) 
[Autodesk.Revit.DB ModelText](3a51d58c-3e29-b641-e8bb-4d8a17c31527.htm) 
[Autodesk.Revit.DB MultipleValuesIndicationSettings](f23f984b-7cbf-54be-b2b9-a7069adaa339.htm) 
[Autodesk.Revit.DB MultiReferenceAnnotation](2224ac33-d7c0-bda8-70de-0005023c2149.htm) 
[Autodesk.Revit.DB MultiSegmentGrid](8488ef7c-7669-26a7-8088-dd78e96850de.htm) 
[Autodesk.Revit.DB NestedFamilyTypeReference](ff71e3b0-4300-7d04-1356-a045b9a90407.htm) 
[Autodesk.Revit.DB NumberingSchema](Numbering-Schema-Class.md) 
[Autodesk.Revit.DB NumberSystem](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm) 
[Autodesk.Revit.DB Opening](720de864-9f4e-c606-c7f4-2e7a0b2da46f.htm) 
[Autodesk.Revit.DB ParameterElement](2ad60b36-07d6-6aed-62c7-89f388f05ffb.htm) 
[Autodesk.Revit.DB Part](1ee04db6-195f-58fa-a245-5a2f2d404200.htm) 
[Autodesk.Revit.DB PartMaker](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm) 
[Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm) 
[Autodesk.Revit.DB PhaseFilter](3236c80e-48be-f657-951f-70490a43f065.htm) 
[Autodesk.Revit.DB.Plumbing PipeSettings](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm) 
[Autodesk.Revit.DB PrintSetting](4d303fcb-ff74-de75-933a-3e8d47d11716.htm) 
[Autodesk.Revit.DB ProjectInfo](e90b12f3-9bf4-f536-3556-c9944cbf9f38.htm) 
[Autodesk.Revit.DB PropertyLine](780ace09-16a7-b622-d04d-05998be8eebb.htm) 
[Autodesk.Revit.DB PropertySetElement](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm) 
[Autodesk.Revit.DB ReferencePoint](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm) 
[Autodesk.Revit.DB Revision](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm) 
[Autodesk.Revit.DB RevisionCloud](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm) 
[Autodesk.Revit.DB RevisionNumberingSequence](52b6f8d8-4d5e-dfee-7782-5cd7a77ee543.htm) 
[Autodesk.Revit.DB RevisionSettings](599f75fc-d2b6-63b3-7295-0c314415b638.htm) 
[Autodesk.Revit.DB ScheduleSheetInstance](68db8e46-90de-6b54-3dae-598957d94201.htm) 
[Autodesk.Revit.DB Segment](8505c96c-1ed1-8c1d-20d7-6661781d0b3c.htm) 
[Autodesk.Revit.DB SheetCollection](80b4a5d7-4be8-41ce-1fd7-9f1fa3d9c241.htm) 
[Autodesk.Revit.DB SketchBase](11df9ef5-c21a-8e70-f3d8-f6d131b36221.htm) 
[Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm) 
[Autodesk.Revit.DB SpatialElement](e73594e8-23aa-899f-82fb-3490def8ece2.htm) 
[Autodesk.Revit.DB SpatialElementCalculationLocation](f4fed5e0-0964-a973-c8f5-7beb046a2849.htm) 
[Autodesk.Revit.DB SpatialElementTag](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm) 
[Autodesk.Revit.DB SSEPointVisibilitySettings](5bd4779b-340d-8509-2376-1f97f828bf42.htm) 
[Autodesk.Revit.DB StartingViewSettings](aaa6f49c-faeb-851e-45e9-d3d5799c1753.htm) 
[Autodesk.Revit.DB.Structure AnalyticalElement](../Autodesk.Revit.DB.Structure/Analytical-Element-Class.md) 
[Autodesk.Revit.DB.Structure AnalyticalLink](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm) 
[Autodesk.Revit.DB.Structure AnalyticalToPhysicalAssociationManager](0f7f395b-3f70-aa6e-e584-b70c11f767ad.htm) 
[Autodesk.Revit.DB.Structure AreaReinforcement](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm) 
[Autodesk.Revit.DB.Structure BoundaryConditions](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm) 
[Autodesk.Revit.DB.Structure FabricArea](../Autodesk.Revit.DB.Structure/Fabric-Area-Class.md) 
[Autodesk.Revit.DB.Structure FabricSheet](../Autodesk.Revit.DB.Structure/Fabric-Sheet-Class.md) 
[Autodesk.Revit.DB.Structure Hub](../Autodesk.Revit.DB.Structure/Hub-Class.md) 
[Autodesk.Revit.DB.Structure LoadBase](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm) 
[Autodesk.Revit.DB.Structure LoadCase](2a215599-9c4c-d817-e170-605fd705699d.htm) 
[Autodesk.Revit.DB.Structure LoadCombination](82891124-6fb9-e612-ca8c-6f4e32e2c121.htm) 
[Autodesk.Revit.DB.Structure LoadNature](0c83b295-7a01-105b-2ae7-29e6c37be32d.htm) 
[Autodesk.Revit.DB.Structure LoadUsage](0b44bcfe-4c5e-85c2-adb5-aeb6ad097ee6.htm) 
[Autodesk.Revit.DB.Structure PathReinforcement](1593a849-b883-73d4-7c02-a2522877d71d.htm) 
[Autodesk.Revit.DB.Structure Rebar](../Autodesk.Revit.DB.Structure/Rebar-Class.md) 
[Autodesk.Revit.DB.Structure RebarContainer](../Autodesk.Revit.DB.Structure/Rebar-Container-Class.md) 
[Autodesk.Revit.DB.Structure RebarCoupler](af258367-f0c5-e4d3-f863-1733d7bf6b30.htm) 
[Autodesk.Revit.DB.Structure RebarInSystem](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm) 
[Autodesk.Revit.DB.Structure ReinforcementSettings](../Autodesk.Revit.DB.Structure/Reinforcement-Settings-Class.md) 
[Autodesk.Revit.DB.Structure StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.htm) 
[Autodesk.Revit.DB.Structure StructuralConnectionSettings](e70eb9af-6795-63d0-417f-40806ee73f8f.htm) 
[Autodesk.Revit.DB.Structure StructuralSettings](../Autodesk.Revit.DB.Structure/Structural-Settings-Class.md) 
[Autodesk.Revit.DB.Structure Truss](e0cdc591-cac6-57c7-6190-f0d48cc0e4a9.htm) 
[Autodesk.Revit.DB SunAndShadowSettings](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm) 
[Autodesk.Revit.DB TextElement](013e58c3-f3d2-d976-89f0-ff4ff701951d.htm) 
[Autodesk.Revit.DB View](View-Class.md) 
[Autodesk.Revit.DB ViewNavigationToolSettings](62a69b5d-082a-85f5-e568-f15ccfec1164.htm) 
[Autodesk.Revit.DB Viewport](Viewport-Class.md) 
[Autodesk.Revit.DB ViewPosition](View-Position-Class.md) 
[Autodesk.Revit.DB ViewSheetSet](5553be2c-8ce7-cbc1-b99e-85c74bcf28d3.htm) 
[Autodesk.Revit.DB WorksetDefaultVisibilitySettings](8a6f0949-069b-4b83-380c-f6582ef37a40.htm) 
[Autodesk.Revit.DB WorksharingDisplaySettings](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)
