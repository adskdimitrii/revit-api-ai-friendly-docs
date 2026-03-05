# Exporter IFC Methods

Source: https://www.revitapidocs.com/2026/0ac7b8c2-ed96-fcea-cd1d-4fa4d205fc19.htm

---

| Exporter IFC Methods |
| --- |

The [ExporterIFC](Exporter-IFC-Class.md) type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddBuildingStorey](Exporter-IFC-Add-Building-Storey-Method.md) | **Obsolete.** Adds building storey to the exporter's internal cache. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearFaceWithElementHandleMap](5f97a843-1df7-64fb-f063-2e8f4899774d.htm) | Clear face with element handle map. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](daa92a17-48ad-264e-8a7d-d2a8de070508.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [FindSpaceBoundingElementHandle](facc8372-3b66-2b31-135c-852985763186.htm) | Looks up the handle associated to the element and level id from the ExporterIFC's internal cache. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Get3DContextHandle](e1ea52a9-9e2c-9704-cfab-d43fe87fd53b.htm) | Obtains the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities). |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDoorWindowOpeningHandle](aa17a626-7f33-0984-6b2d-e8ff8b7e6423.htm) | Get the handle to the opening associated with a hosted (door/window) element from the internal cache. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFamilyInstanceAssemblyOffset](Exporter-IFC-Get-Family-Instance-Assembly-Offset-Method.md) | Obtains Translation to adjust Family Instance within an Assembly, based on Family Symbol origin change. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFamilyName](bbab76a2-98c3-e6d3-c8b2-829ebd5e45e5.htm) | Gets the name of the element assigned to the current export state. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFile](1baac5bf-ee32-4d1c-0ba3-6193124c0d9c.htm) | Gets the handle to the IFC file being created during this export operation. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetHostObjects](39ace44e-26a7-e530-2dc2-737a1e3f1479.htm) | Returns a collection containing the host object handles in the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayerNameForPresentationLayer](9bb2d5c4-40ef-661b-b49e-720e74a1ca57.htm) | Get the layer name associated with an element from the default layer mapping table. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLevelInfo](Exporter-IFC-Get-Level-Info-Method.md) | **Obsolete.** Returns an object representing the information about a level in the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLevelInfos](Exporter-IFC-Get-Level-Infos-Method.md) | **Obsolete.** Returns a collection containing the information about all levels in the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialIdForCurrentExportState](ea78908e-959b-dca9-06a2-abce0c4cef70.htm) | This gets the material id that is associated with the element in the current export state. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOptions](79e15a6b-3a5d-3aa1-c13a-5155356c5842.htm) | Gets the collection of named options set by the exporter client. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOrCreateFillPattern](13faad3d-86f3-ed60-b3a3-78504c969716.htm) | Get (or create) the IfcFillPatternStyle associated with an ElementId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPresentationLayerAssignments](7dad2ed6-30a7-1b25-5e5f-8a1d7389f103.htm) | Get the list of the internally IfcPresentationLayerAssignments and their respective shape representations. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRelatedElements](dbab0f38-a7d9-8f42-5217-c41c8a5330f7.htm) | Gets all elements not associated to stories. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRelatedProducts](fa71bbad-420e-d073-7012-da63f6f4bd3e.htm) | Gets all products not associated to stories. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PopExportState](719e062b-eea9-3010-33ad-e48dae367276.htm) | Resets the internal state of the exporter to process the previously active input element (if any), or  the default state if the stack is empty. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PopTransform](004039fe-8364-af98-6a51-7df026ea4fc0.htm) | Resets the internal transform of the exporter to process the previously active input element (if any), or  the default transform if the stack is empty. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PushExportState](84dee1b6-d008-e039-6f06-6e984920228c.htm) | Sets the internal state of the exporter to process the geometry and properties of the input element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PushTransform](bc1f8a42-7cbc-600a-9d1f-bcf80d6186e0.htm) | Sets the internal transform of the exporter to process the geometry and properties of the input element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RegisterDoorWindowForUncreatedOpening](688b2144-693c-544c-45db-e6257d21430b.htm) | Registers a door or window in the ExporterIFC's internal cache. The ids registered correspond to  openings in walls which have not been processed and created yet. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RegisterFaceWithElementHandle](f002582a-79a1-23b6-4278-2fabcb133444.htm) | Register face with element handle to make sure the openings created are related to the right element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RegisterSpaceBoundingElementHandle](9e2dc4fb-c062-f68d-af7f-fbbe7bd359e1.htm) | Stores a handle representing a space bounding element to the ExporterIFC's internal cache. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveBuildingStorey](Exporter-IFC-Remove-Building-Storey-Method.md) | **Obsolete.** Removes an IFCLevelInfo corresponding to a level from the exporter's internal cache. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Set3DContextHandle](94faf2de-158e-87bc-a9e0-ad0e6ff8eedc.htm) | Sets the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities). |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetCurrentExportedDocument](f0af06ac-6928-c772-54b8-46070927d5e1.htm) | Sets the exporter to process a particular document during export. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFile](30eb507b-8796-ce4e-ec59-1684e1306a0f.htm) | Sets the handle to the IFC file being created during this export operation. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetMaterialIdForCurrentExportState](af494e73-5135-bd2b-8d71-389fa5be3ec7.htm) | This sets the material id that is to be associated with the element in the current export state. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetOwnerHistoryHandle](dbdb1fba-2cbb-1c18-56b8-f6f35bde1f3f.htm) | Sets the handle to the IfcOwnerHistory for the file. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
