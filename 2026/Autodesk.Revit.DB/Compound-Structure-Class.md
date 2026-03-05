# Compound Structure Class

Source: https://www.revitapidocs.com/2026/dc1a081e-8dab-565f-145d-a429098d353c.htm

---

| Compound Structure Class |
| --- |

Describes the internal structure of a wall, floor, roof or ceiling. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB CompoundStructure 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class CompoundStructure : IDisposable
```

```
Public Class CompoundStructure
	Implements IDisposable
```

```
public ref class CompoundStructure : IDisposable
```

```
type CompoundStructure = 
    class
        interface IDisposable
    end
```
The CompoundStructure type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CutoffHeight](50227765-fb72-587a-38aa-0559877a790f.htm) | Horizontal segments below or at the cutoff height have their distance to the wall bottom fixed, those above  have their distance to the wall top fixed. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndCap](545d437e-a6b3-bfcb-97c2-d16106669744.htm) | Indicates the end cap condition defining which shell layers will participate in end wrapping. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HasStructuralDeck](0a185ddd-e618-7b5b-ba1d-6d659ae79d7d.htm) | Checks if the compound structure has a structural deck. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsEmpty](83b951b2-dadd-ac46-82e6-40003a29403e.htm) | Checks whether this CompoundStructure is empty. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](8b536d01-26ab-721a-9047-db61124ecef0.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsVerticallyCompound](cd352f22-8ca4-b3b6-f247-d9865a91bb6f.htm) | Identifies if this CompoundStructure represents a layout that is more complicated than a simple set of parallel layers. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LayerCount](8598a249-81da-128f-8629-0bcb2c8f3c3c.htm) | Returns the number of layers contained in this CompoundStructure. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MinimumSampleHeight](fe47d724-5e94-dc16-903b-3f2dc51e3c56.htm) | The minimum sample height determined by the current sample height and the horizontal segments. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [OpeningWrapping](f13813ad-738a-9cd3-2fad-02aba0c0b5f9.htm) | Indicates the opening wrapping condition defining which shell layers of a wall, in plan view, wrap at inserts and openings. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SampleHeight](8b60783a-a146-a498-0d92-3d5e55dab34e.htm) | The sample height is the presumed height of the wall to which the data in this CompoundStructure is applied. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [StructuralMaterialIndex](cf4d771e-6ed2-ec6a-d32d-647fb5b649b3.htm) | Indicates the layer whose material defines the structural properties of the type for the purposes of analysis. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VariableLayerIndex](e93ce781-df22-cc64-7ad8-70a0d6bc7707.htm) | Indicates the index of the layer which is designated as variable. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddWallSweep](3f95013f-ae34-e068-96b5-a930fb26d2a5.htm) | Adds a new wall sweep or reveal to the compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AssociateRegionWithLayer](Compound-Structure-Associate-Region-With-Layer-Method.md) | Associates a region with a layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanLayerBeStructuralMaterial](68844a06-8e4c-2647-946e-13bb7f7b0816.htm) | Identifies if the input layer can be designated as defining the structural material for this structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanLayerBeVariable](b2a3d8c3-39e0-d924-2047-32015ba66075.htm) | Identifies if the input layer can be designated as a variable thickness layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanLayerWidthBeNonZero](Compound-Structure-Can-Layer-Width-Be-Non-Zero-Method.md) | Identifies if changing the width of an existing layer from zero to a positive value will create a rectangular region. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanSplitAndMergeRegionsBeUsed](58111c1e-6a6a-a123-522f-6a781588a8a8.htm) | Checks whether split and merge regions operations can be used for this compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ChangeRegionWidth](b4005b2b-b7eb-f191-90ef-32cf9cd3d03a.htm) | Adjust the width of an existing simple region. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearWallSweeps](afc7fce6-66db-aa6f-6afe-85dd4bf2578b.htm) | Removes all sweeps or reveals from the compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CreateSimpleCompoundStructure](b4ef2a78-a4c3-8bf6-2709-945f03954ff8.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CreateSingleLayerCompoundStructure(MaterialFunctionAssignment, Double, ElementId)](daabdba6-a85c-aed1-927a-7ff9e519489f.htm) | Creates a CompoundStructure containing a single layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CreateSingleLayerCompoundStructure(Double, MaterialFunctionAssignment, Double, ElementId)](d1a7a3ba-717c-a939-2161-dc22a94b8824.htm) | Creates a vertically compound CompoundStructure with one layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeleteLayer](Compound-Structure-Delete-Layer-Method.md) | Deletes the specified layer from this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](20914736-3ee9-d59f-27da-58468ea9d05c.htm) | Releases all resources used by the CompoundStructure |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [FindEnclosingRegionAndSegments](e5a63d60-6fa3-f414-20b5-ef72da637849.htm) | Given a pair of grid coordinates, and a direction for splitting, returns the enclosing region and the two segments  intersected by a line through the grid point. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAdjacentRegions](2749034b-a043-be0a-7400-1cdbbef24c76.htm) | Gets the ids of region bound to a specified segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetCoreBoundaryLayerIndex](33a4b0ce-7694-bf4f-81a0-a8b66fa3cade.htm) | Returns the index of the layer just below the core boundary. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDeckEmbeddingType](Compound-Structure-Get-Deck-Embedding-Type-Method.md) | Retrieves the deck embedding type used for the specified structural deck. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDeckProfileId](Compound-Structure-Get-Deck-Profile-Id-Method.md) | Retrieves the profile loop used for the specified structural deck. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExtendableRegionIds](75834253-b686-6284-46ab-a60d45f4c6a2.htm) | Gets the extendable region ids for the compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFirstCoreLayerIndex](db2884a9-bd2a-e7be-eb95-d8dd5e74ee59.htm) | Gets the index of the first core layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLastCoreLayerIndex](4e32008c-8d6a-5368-a4d9-4e3e103bce9d.htm) | Gets the index of the last core layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayerAssociatedToRegion](60537f57-d0f8-082d-3181-a6097550730d.htm) | Gets the layer associated to a particular region. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayerFunction](Compound-Structure-Get-Layer-Function-Method.md) | Retrieves the function of the specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayerPriority](Compound-Structure-Get-Layer-Priority-Method.md) | Retrieves the priority of the specified layer.  Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayers](105b59e9-9cea-1988-a5a7-cc9cde49145c.htm) | A copy of the layers which define this compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLayerWidth](Compound-Structure-Get-Layer-Width-Method.md) | Retrieves the width of a specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetMaterialId](Compound-Structure-Get-Material-Id-Method.md) | Retrieves the material element id of a specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetMinimumLayerThickness](e2785666-33ac-105e-cf2a-a5f4bff43b4f.htm) | Get the minimum allowable layer thickness. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfShellLayers](Compound-Structure-Get-Number-Of-Shell-Layers-Method.md) | Retrieves the number of interior or exterior shell layers. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOffsetForLocationLine](6deb6602-4fdc-a01e-170c-e8a3e953bc4b.htm) | Returns the offset from the center of the compound structure to the given location line value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPreviousNonZeroLayerIndex](98a0b5c3-e17e-661c-9668-1cb535241ff5.htm) | Returns the index of the nearest non\-zero width layer before this layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRegionEnvelope](ab2f1bd3-bd9b-5f73-4a0d-0af599bcc173.htm) | Gets the envelope that a specified region spans. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRegionIds](f0349b61-d48a-e5e6-143c-1e2a63069e9f.htm) | Gets the region ids of this compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRegionsAlongLevel](484c680f-0545-bb6e-c987-ba813751db2c.htm) | Returns the ids of the regions encountered as the vertically compound structure is traversed  at a constant height above the bottom a wall to which this structure is applied. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetRegionsAssociatedToLayer](Compound-Structure-Get-Regions-Associated-To-Layer-Method.md) | Gets the set of region ids associated to a particular layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSegmentCoordinate](d729ba6f-a98f-98b3-43f9-60f63fbd834b.htm) | Gets the coordinate of a segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSegmentEndPoints](4e6f1ee9-53cf-15fd-0e6e-f684941f107a.htm) | Gets the end points of a segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSegmentIds](1d87764d-287c-2cf8-c9d9-4184fe7e40e9.htm) | Gets the segment ids of this compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSegmentOrientation](9f4b22d2-8bc1-4e07-9f5a-aebc92cb3e38.htm) | Gets the orientation of a segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetSimpleCompoundStructure](9c3b9719-8d01-4db3-4cb1-69a8a70f37ac.htm) | Takes a horizontal slice through a sample wall to which this CompoundStructure is applied  and returns a simple compound structure which describes that slice, i.e. a series of  parallel layers. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetWallSweepsInfo](f8140797-a9ac-234b-cb54-5a1c56ce45bf.htm) | Obtains a list of the intrinsic wall sweeps or reveals in this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetWidth](fcd2ffc8-05bc-5d3c-f4e2-b62d5a3376ce.htm) | The width implied by this compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetWidth(Int32\)](668c8be8-3a70-9362-29ae-7fdc07988394.htm) | Computes the width of the envelope (2d bounding box) of the specified region. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCoreLayer](Compound-Structure-Is-Core-Layer-Method.md) | Checks if the specified layer is a core layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsEqual](e42daee6-b3c8-3c65-d26c-3bbff6598479.htm) | Checks whether this CompoundStructure is the same as another CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsLayerValid](Compound-Structure-Is-Layer-Valid-Method.md) | Verifies that the data in this layer is internally consistent. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsRectangularRegion](95361f1e-ea42-932a-3417-7238c4558e0c.htm) | Determines whether the specified region is rectangular. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsSimpleRegion](49160dba-ba08-a7e8-5b99-770d33a8e325.htm) | Determines whether the region is a simple region in this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsStructuralDeck](bf8e5810-eb9e-125b-21bb-d43e406c6c39.htm) | Determines whether a specified layer is a structural deck. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValid](e77d2eba-f2fd-b2f6-c008-ccf45826a784.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidLayerPriority](Compound-Structure-Is-Valid-Layer-Priority-Method.md) | Checks if the layer priority is valid to match the function. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidRegionId](2497dbbd-18fd-0e88-e85c-f456327b8ee4.htm) | Determines whether the specified integer is actually the id of a region in this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidSampleHeight](28d6814a-099a-1f81-0bd1-90505a7a5fdf.htm) | Is the specified height a valid sample height for this compound structure? |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidSegmentId](680bccec-130e-238e-4b41-bbbcac24fdb8.htm) | Determines whether the specified integer is actually the id of a segment in this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsVerticallyHomogeneous](7f06ea80-ba2f-aecb-be51-cb463769ae1b.htm) | Indicates whether this CompoundStructure represents a single set of parallel layers. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [MergeRegionsAdjacentToSegment](ebc23bae-07f1-b48c-8cfa-dcb8850cb723.htm) | Merges the two regions which share the specified segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ParticipatesInWrapping](Compound-Structure-Participates-In-Wrapping-Method.md) | Identifies if a layer is included in wrapping at inserts and ends. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveWallSweep](e3f2b69a-e4ea-5781-8285-6c2e183933a8.htm) | Removes a single sweep or reveal from the compound structure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ResetAllLayersPriorities](Compound-Structure-Reset-All-Layers-Priorities-Method.md) | Resets all the priorities of all layers to the default priorities defined by their functions. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ResetLayerPriority](Compound-Structure-Reset-Layer-Priority-Method.md) | Resets the priority of the specific layer to the default priority defined by its function. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetDeckEmbeddingType](Compound-Structure-Set-Deck-Embedding-Type-Method.md) | Sets the deck embedding type to use for the specified structural deck. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetDeckProfileId](Compound-Structure-Set-Deck-Profile-Id-Method.md) | Sets the profile loop to use for the specified structural deck. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetExtendableRegionIds](2d4b6163-0425-9c97-3d17-1087243e4cc5.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayer](Compound-Structure-Set-Layer-Method.md) | Sets a single layer for this CompoundStructure. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayerFunction](Compound-Structure-Set-Layer-Function-Method.md) | Sets the function of the specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayerPriority](Compound-Structure-Set-Layer-Priority-Method.md) | Sets the priority of the specific layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayers](0392b682-451d-5399-54b5-44373ce941c6.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLayerWidth](Compound-Structure-Set-Layer-Width-Method.md) | Sets the width of a specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetMaterialId](Compound-Structure-Set-Material-Id-Method.md) | Sets a material element for a specified layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetNumberOfShellLayers](Compound-Structure-Set-Number-Of-Shell-Layers-Method.md) | Sets the number of interior or exterior shell layers. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetParticipatesInWrapping](Compound-Structure-Set-Participates-In-Wrapping-Method.md) | Assigns if a layer is included in wrapping at inserts and ends. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SplitRegion(UV, RectangularGridSegmentOrientation)](8db1791b-4b60-6edb-81bf-908a673b3baa.htm) | Splits the region which contains the specified grid point by a line with the specified direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SplitRegion(UV, RectangularGridSegmentOrientation, Int32 )](7da2c89e-7c21-4e8b-f86c-e8d6604aaf9a.htm) | Splits the region which contains the specified grid point by a line with the specified direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A compound structure consists a collection of ordered layers, proceeding from exterior to interior for a wall, or from top to bottom for a
 floor, roof or ceiling. The properties of these layers determine the
 thickness, material, function and priority of the overall structure of the associated wall, floor, roof or ceiling. Layers can
 be accessed via the [GetLayers](105b59e9-9cea-1988-a5a7-cc9cde49145c.htm) method and completely replaced using SetLayers. Layers
 can also be accessed and modified individually using the "layer index", which is a value from in the range \[0, LayerCount)
 identifying the layer in the structure. 

A structure supports the concept of "core layers" and "shell layers". There are two layer indices which identify
 where the boundary between core and shell layers occur in the list of layers. The boundaries between shell and core layers
 are identifiable using [GetFirstCoreLayerIndex](db2884a9-bd2a-e7be-eb95-d8dd5e74ee59.htm) , [GetLastCoreLayerIndex](4e32008c-8d6a-5368-a4d9-4e3e103bce9d.htm) , [GetCoreBoundaryLayerIndex(ShellLayerType)](33a4b0ce-7694-bf4f-81a0-a8b66fa3cade.htm) or [GetNumberOfShellLayers(ShellLayerType)](Compound-Structure-Get-Number-Of-Shell-Layers-Method.md) . The core layer boundary can be changed with [SetNumberOfShellLayers(ShellLayerType, Int32\)](Compound-Structure-Set-Number-Of-Shell-Layers-Method.md) . 

Compound structures may be vertically compound. If [IsVerticallyCompound](cd352f22-8ca4-b3b6-f247-d9865a91bb6f.htm) is false,
 the CompoundStructure describes a series of parallel layers, each with specified width, function, priority, material and other properties.
 If [IsVerticallyCompound](cd352f22-8ca4-b3b6-f247-d9865a91bb6f.htm) is true (which should apply only for CompoundStructures assigned to walls) then
 horizontal sections at different elevations may have different layered
 structures. In this case, the structure describes a vertical section via a rectangle
 which is divided into polygonal regions whose sides are all vertical or horizontal segments.
 A map associates each of these regions with the index of a layer in the CompoundStructure which
 determines the properties of that region. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
